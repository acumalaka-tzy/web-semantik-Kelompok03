# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal - alidvaRoelyaPadang_251402007

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 / 10 kota unik
- Mengapa tidak (atau mengapa tepat) 30 triple: Ya, mencapai 30 triple,Klausa LIMIT 10 di dalam WHERE membatasi jumlah baris pencocokan pola (solution mapping) sebanyak 10 baris, bukan membatasi jumlah triple. Karena ke-10 baris yang keluar memiliki subjek kota yang seluruhnya unik (tidak ada kota yang muncul dua kali), maka setiap baris akan mengisi 3 pola di blok CONSTRUCT dan menghasilkan 10 x  3 = 30 triple yang semuanya unik.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 49 triple, film tanpa tanggal: 15
- Sumber data: DBpedia
- Triple yang tetap tercetak untuk film tanpa tanggal: Triple yang tetap tercetak adalah `?film a schema:Movie`, `?film schema:name ?judul`, dan `?film schema:director dbr:Christopher_Nolan`, sedangkan triple `?film schema:datePublished ?rilis` tidak tercetak. Tidak ada pesan error karena klausa `OPTIONAL` membiarkan variabel `?rilis` tetap kosong (*unbound*) saat film tidak memiliki `dbo:releaseDate`, dan spesifikasi SPARQL `CONSTRUCT` secara otomatis melewati pembentukan pola triple yang mengandung variabel *unbound* tanpa menggagalkan eksekusi query.
- Query lokal tanpa internet: Menjalankan `Q_TANPA_TANGGAL` saja tetap berhasil karena `rdflib` membaca graf RDF langsung dari berkas lokal `film_nolan.ttl` yang sudah tersimpan di komputer sehingga tidak memerlukan koneksi jaringan. Sebaliknya, jika seluruh `demo_c.py` dijalankan ulang tanpa internet, program akan berhenti dan menghasilkan pesan error koneksi (`URLError` / `gaierror`) pada baris `sp.queryAndConvert()` karena gagal menghubungi endpoint jarak jauh `https://dbpedia.org/sparql`.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: Karena saat membangun graf lokal melalui `CONSTRUCT` pada `q_demo_b.rq`, tipe kelas setiap film telah ditransformasikan menjadi `schema:Movie` (`?film a schema:Movie`). Akibatnya, kelas asli `dbo:Film` dari DBpedia tidak ikut tertulis di dalam berkas `film_nolan.ttl`, sehingga pencarian menggunakan `dbo:Film` menghasilkan 0 kecocokan.

Bagian C - Materialisasi
- Output demo_d.py: Sebelum: 0, Sesudah: 3, Ada Rina: 3
- Mengapa Ada Rina bernilai 3: Karena materialisasi menggunakan query `CONSTRUCT` pada `rdflib` bersifat satu kali jalan (*one-shot evaluation*), bukan *live reasoner* otomatis. Saat fakta baru (`ex:rina a ex:DosenTetap`) ditambahkan ke dalam graf `g` setelah blok `CONSTRUCT` selesai dijalankan, aturan inferensi `?x a/rdfs:subClassOf* ?super` tidak dieksekusi ulang secara otomatis, sehingga triple turunan `ex:rina a foaf:Person` belum terbentuk di dalam graf `g` ketika `Q_ORANG` dijalankan.
- Output materialisasi_ulang.py: Putaran 1: 4 triple baru | Person: 3, Rina masuk | Person: 3, Putaran 2 | Person: 4, Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: `ex:budi a ex:DosenTetap`, `ex:sari a ex:Dosen`, dan `ex:andi a ex:Mahasiswa`. Ketiga triple ini ikut dihasilkan oleh query `CONSTRUCT` karena sifat refleksif operator `*` (jalur 0 langkah pada `rdfs:subClassOf*`), tetapi karena ketiganya sudah ada secara eksplisit di dalam `kampus.ttl` sejak awal, kondisi `if t not in g` menyaring ketiganya sehingga tidak dihitung sebagai triple baru (dan tidak dimasukkan ke `kampus_turunan.ttl`).
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: Kegunaan `kampus_turunan.ttl` adalah memisahkan fakta hasil inferensi (6 triple turunan) dari fakta asli/eksplisit (`kampus.ttl`), sehingga data sumber tetap bersih, mudah diaudit, serta triple turunan dapat dihapus atau dibuat ulang kapan saja jika aturan hierarki kelas berubah tanpa merusak data asli. Langkah manual yang masih tersisa adalah memanggil ulang fungsi `materialisasi(g)` secara eksplisit setiap kali ada penambahan data baru (serta melakukan *re-materialization* dari awal terhadap `kampus.ttl` apabila ada penghapusan atau perubahan data lama, karena menghapus fakta dasar tidak otomatis mencabut triple turunan yang sudah telanjur disimpan).

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong, tanpa error | Baris `CONSTRUCT { ?film ex:judul ?j . }` memakai variabel `?film` yang tidak terikat (*unbound*) karena pada `WHERE` baris `?f dbo:director dbr:Christopher_Nolan` variabel film ditulis sebagai `?f`. | 3 triple (masing-masing satu `ex:judul` untuk `dbr:Following`, `dbr:Memento`, dan `dbr:Insomnia`) |
| rusak_b | 4 triple | Dua nilai yang tampak sama | Baris `?o foaf:name\|rdfs:label\|schema:name ?n .` mengambil dua literal nama `dbr:Christopher_Nolan` yang berbeda tag bahasa (`"Christopher Nolan"` tanpa tag dari `foaf:name` dan `"Christopher Nolan"@en` dari `rdfs:label`) sehingga dianggap sebagai dua triple berbeda oleh RDF. | 3 triple (tepat satu `ex:nama` tanpa tag bahasa untuk `dbr:Christopher_Nolan`, `dbr:Joko_Anwar`, dan `dbr:Mira_Lesmana`) |
| rusak_c | 0 triple | Superkelas tidak ditemukan | Baris `?x a ex:Permukiman .` pada `WHERE` tidak memakai jalur properti `a/rdfs:subClassOf*`, padahal Medan, Surabaya, dan Tomok dideklarasikan sebagai instan dari subkelas `ex:Permukiman`. | 3 triple (`ex:Medan`, `ex:Surabaya`, dan `ex:Tomok` bertipe `ex:Permukiman`) |
## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | [isi] | [isi] |
| 2 LIMIT | [isi] | [isi] |
| 3 Simpan, jangan ulangi | [isi] | [isi] |
| 4 Jangkar jalur | [isi] | [isi] |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: [isi]

### Diskusi 1 - Taksonomi berubah
[150-250 kata]

### Diskusi 2 - SELECT atau CONSTRUCT
[150-250 kata]

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | [isi] |
| 2 | [isi] |
| 3 | [isi] |
| 4 | [isi] |
| 5 | [isi] |
