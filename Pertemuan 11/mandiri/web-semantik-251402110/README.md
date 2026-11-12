# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

**Nama:** Muhammad Izyan Roshan 
**NIM:** 251402110

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 baris / 10 kota unik
- Mengapa tidak (atau mengapa tepat) 30 triple: 
  Graf RDF adalah himpunan, jadi triple yang identik hanya dihitung satu kali. Kalau satu kota muncul di lebih dari satu solution, sebagian triple-nya kembar dan menyusut. Penyebab satu kota muncul berkali-kali:
  - Kota punya lebih dari satu nilai populasi (wdt:P1082), sehingga tiap nilai jadi solution sendiri.
  - Kota punya beberapa jalur wdt:P31 / wdt:P279* menuju wd:Q515, sehingga baris yang sama muncul ganda.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia (https://dbpedia.org/sparql)
- Triple yang tetap tercetak untuk film tanpa tanggal: 
  - Tetap tercetak: ?film a schema:Movie, ?film schema:name ?judul, dan ?film schema:director dbr:Christopher_Nolan. Ketiganya tidak memakai ?rilis.
  - Tidak tercetak: ?film schema:datePublished ?rilis, karena ?rilis tidak terikat.
  - Mengapa tidak ada error: releaseDate berada di OPTIONAL, jadi film tetap lolos sebagai solution walau ?rilis kosong. Menurut spesifikasi SPARQL, pola template yang memuat variabel tak terikat dilewati diam-diam. Itu perilaku normal, bukan kesalahan.
- Query lokal tanpa internet:
  - Hanya Q_TANPA_TANGGAL pada film_nolan.ttl: berhasil karena data sudah ada di berkas lokal. Graph().parse("film_nolan.ttl") membaca dari disk, dan query() dijalankan rdflib di memori tanpa koneksi ke endpoint.
  - Menjalankan ulang seluruh demo_c.py: gagal di sp.queryAndConvert() dengan error koneksi (misalnya URLError), karena langkah pertamanya mengirim query ke https://dbpedia.org/sparql. Program berhenti sebelum print dan serialize, jadi tidak ada output baru dan film_nolan.ttl lama tidak berubah.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl:
  -film_nolan.ttl hanya berisi hasil template CONSTRUCT, dan template itu menulis tipe schema:Movie. Triple a dbo:Film ada di data sumber DBpedia, bukan di template, jadi tidak ikut tersimpan. rdflib juga tidak melakukan inferensi, sehingga tidak ada yang menyamakan schema:Movie dengan dbo:Film. Karena memakai COUNT, hasilnya satu baris n = 0, bukan hasil kosong.

## Bagian C - Materialisasi
- Output demo_d.py: 
  Sebelum: 0
  Sesudah: 3
  Ada Rina: 3
- Mengapa Ada Rina bernilai 3:
  Query ?x a foaf:Person hanya mencocokkan triple yang tertulis langsung di graf. rdflib tidak melakukan inferensi, jadi ia tidak otomatis menurunkan bahwa subkelas adalah foaf:Person.
  - Sebelum (0): tidak ada triple a foaf:Person sama sekali. Budi, Sari, dan Andi hanya bertipe ex:DosenTetap, ex:Dosen, dan ex:Mahasiswa.
  - Sesudah (3): CONSTRUCT dengan a/rdfs:subClassOf* menelusuri rantai subkelas, lalu g.add(t) menuliskan hasilnya ke graf sebagai triple eksplisit. Budi, Sari, dan Andi kini punya a foaf:Person. Ini disebut materialisasi.
  - Ada Rina (tetap 3): Rina ditambahkan setelah materialisasi, hanya dengan ex:rina a ex:DosenTetap. Materialisasi dijalankan sekali dan tidak diulang, sehingga tidak ada triple ex:rina a foaf:Person. Query tetap 3, bukan 4.
- Output materialisasi_ulang.py:
  Putaran 1: 4 triple baru | Person: 3
  Rina masuk | Person: 3
  Putaran 2 | Person: 4
  Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru:
  ex:budi a ex:DosenTetap
  ex:sari a ex:Dosen
  ex:andi a ex:Mahasiswa
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: 
  Berkas ini hanya berisi triple hasil inferensi (6 triple: 4 dari putaran 1 dan 2 untuk Rina). Di kampus_v4.ttl, triple turunan bercampur dengan data asli dan tidak bisa dibedakan lagi. Dengan berkas terpisah, Anda tahu persis triple mana yang dibuat oleh aturan. Bila ex:Dosen tidak lagi menjadi subkelas foaf:Person, triple turunan yang terkait bisa dicabut tanpa menyentuh data asli.
  Langkah manual:
  - Ubah kampus.ttl, yaitu hapus ex:Dosen rdfs:subClassOf foaf:Person.
  - Buang triple turunan lama dari graf (misalnya g -= turunan, atau muat ulang kampus.ttl asli).
  - Jalankan ulang materialisasi dan simpan kampus_turunan.ttl yang baru.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong, tanpa error | emplate di baris CONSTRUCT { ?film ex:judul ?j . } memakai ?film, padahal WHERE mengikat ?f, jadi variabel template tidak pernah terikat dan triple-nya dilewati diam-diam | ganti ?film menjadi ?f |
| rusak_b | 4 triple | Dua nilai yang tampak sama (beda tag bahasa) | Pada baris ?o foaf:name|rdfs:label|schema:name ?n, foaf:name memberi literal polos dan rdfs:label memberi literal @en. Keduanya literal berbeda sehingga tidak melebur | uang tag bahasa dengan STR(), lalu pakai variabel baru di template |
| rusak_c | 0 triple | Superkelas tidak ditemukan (graf kosong) | Baris ?x a ex:Permukiman mencari tipe yang tertulis langsung, padahal di kota.ttl tidak ada satu pun individu bertipe ex:Permukiman. Medan, Surabaya, dan Tomok hanya bertipe subkelasnya | tambah jalur rdfs:subClassOf* |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak relevan. Query dijalankan lewat antarmuka web query.wikidata.org, yang mengirim identitas klien sendiri | UA = "KelasWebSemantik/1.0 (...)" dan SPARQLWrapper("https://dbpedia.org/sparql", agent=UA). Berisi nama aplikasi dan kontak |
| 2 LIMIT | LIMIT 10 (lalu LIMIT 30) membatasi solution selama eksplorasi | Tidak ada LIMIT, dan memang tidak perlu. Query terjangkar pada dbr:Christopher_Nolan dan hasilnya kecil (16 film, 48 triple) |
| 3 Simpan, jangan ulangi | Tidak relevan. Query hanya dijalankan sekali per variasi di antarmuka web | g.serialize("film_nolan.ttl"), lalu Graph().parse("film_nolan.ttl") untuk query kedua tanpa internet |
| 4 Jangkar jalur | ?kota wdt:P31/wdt:P279* wd:Q515. Ujung kanan jalur terjangkar pada wd:Q515 (kota) | Tidak ada jalur * atau +, jadi aturan ini tidak relevan |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:
  ganti wd:Q515 dengan variabel dan buang filter Indonesia
  Alasannya: 
  Aturan 4 berbunyi: jalur * dan + harus berangkat dari IRI tertentu, bukan dari dua variabel. Di query asli, ?kota wdt:P31/wdt:P279* wd:Q515 punya satu ujung terkunci pada wd:Q515. Saya melanggarnya dengan mengganti wd:Q515 menjadi ?jenis, sehingga kedua ujung jalur menjadi variabel. Saya juga membuang wdt:P17 wd:Q252, karena filter Indonesia itu ikut membatasi ?kota dan bisa menutupi pelanggarannya.

### Diskusi 1 - Taksonomi berubah
Taksonomi berubah setahun kemudian

Misalkan ex:Dosen tidak lagi subkelas foaf:Person. Triple yang kini salah adalah ex:budi a foaf:Person, ex:sari a foaf:Person, dan ex:rina a foaf:Person. ex:andi a foaf:Person tetap sah lewat ex:Mahasiswa, dan budi a ex:Dosen tetap sah lewat DosenTetap ⊂ Dosen.

Masalah kampus_v4.ttl dari C1 adalah berkas itu berisi 13 triple, 9 asli dan 4 hasil materialisasi, tanpa penanda pembeda. andi a foaf:Person tampak sama dengan andi a ex:Mahasiswa, jadi Anda hanya bisa menebak atau membuang semuanya.

kampus_turunan.ttl dari C2 menyimpan 6 triple turunan terpisah (4 dari putaran 1, 2 untuk Rina). Cara menemukan yang salah:
- Ubah kampus.ttl.
- Jalankan ulang materialisasi pada data asli (ditambah fakta Rina) untuk mendapat turunan baru.
- Hitung turunan_lama − turunan_baru.

Selisihnya persis tiga triple di atas, sedangkan tiga lainnya aman. Selisih itu dibuang dari graf produksi dan turunan baru ditambahkan. Pelajaran dari Demo D: materialisasi adalah potret, bukan sambungan hidup. Tanpa catatan asal-usul triple, graf produksi menyimpan kesimpulan basi yang tampak seperti fakta.

### Diskusi 2 - SELECT atau CONSTRUCT
SELECT atau CONSTRUCT

Untuk dashboard populasi saya pakai SELECT, dan untuk menggabungkan tiga sumber saya pakai CONSTRUCT.

Dashboard butuh baris dan angka: satu kota, satu populasi. SELECT mempertahankan setiap solution, jadi masalahnya terlihat. Di Bagian A, LIMIT 10 hanya menghasilkan [isi: jumlah triple Anda] triple, bukan 30, karena [isi: kota Anda] muncul lebih dari sekali. Pada data contoh kota.ttl, Medan punya dua populasi (2.435.252 dan 2.097.610), sehingga tabel SELECT menampilkan Medan dua kali. CONSTRUCT menyembunyikan duplikat itu: hanya ada satu a ex:Kota dan satu label, tetapi dua ex:populasi, dan dashboard tidak tahu mana yang dipakai. Dengan SELECT saya bisa memilih satu nilai secara sadar (misalnya MAX) dan menghitung baris dengan benar.

Untuk tiga sumber, kebutuhannya graf bersama, jadi CONSTRUCT cocok. Tiap sumber diterjemahkan ke satu kosakata (ex:nama, ex:populasi), lalu graf-grafnya digabung sebagai himpunan. rusak_b.rq menunjukkan risikonya. Tiga predikat berhasil disatukan, tetapi Nolan menghasilkan 4 triple, bukan 3, karena "Christopher Nolan" dan "Christopher Nolan"@en berbeda literal. Setelah STR(), keduanya melebur. Saat menggabungkan sumber, tag bahasa dan tipe data harus dinormalkan di template.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | CONSTRUCT mencetak template sekali per solution dan menggabungkan triple kembar. rusak_b.rq setelah perbaikan (D): 4 solution menjadi 3 triple, karena dua nilai Nolan melebur. Bagian A: LIMIT 10 dengan batas atas 30 menghasilkan [isi angka Anda] triple |
| 2 | Triple dengan variabel tak terikat tidak dicetak, tanpa error. rusak_a.rq (D): ?film tidak terikat, hasilnya 0 triple. B2: film_nolan.ttl berisi 16 film × 3 triple = 48 triple, tanpa satu pun schema:datePublished |
| 3 | UNION, jalur "|", dan VALUES menyatukan predikat berbeda. rusak_b.rq (D): VALUES ditambah "foaf:name|rdfs:label|schema:name" menyatukan tiga predikat dari tiga orang menjadi ex:nama, dengan hasil akhir 3 triple |
| 4 | Jalur + dan * menelusuri hierarki tanpa menyebut perantara. perbaikan_c.rq (D): a/rdfs:subClassOf* mengubah hasil dari 0 menjadi 3 triple (Medan, Surabaya, Tomok) tanpa menyebut ex:Kota, ex:Desa, atau ex:KotaMetropolitan. C1: Person naik dari 0 menjadi 3 |
| 5 | Materialisasi menyimpan kesimpulan, tetapi harus dihitung ulang. C1: setelah Rina masuk, Person tetap 3. C2: setelah putaran 2 menjadi 4, dan kampus_turunan.ttl berisi 6 triple |
