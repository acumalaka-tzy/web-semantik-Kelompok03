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
## Bagian E - Etika Endpoint dan Diskusi

### E1 - Etika endpoint
| Aturan | Pemeriksaan pada `a_kota_limit.rq` | Pemeriksaan pada `demo_c.py` |
|--------|------------------------------------|------------------------------|
| **1. User-Agent bermakna** | Tidak relevan langsung di dalam teks query `.rq` karena header HTTP diatur oleh aplikasi klien atau browser saat mengirim request. | Dipenuhi pada baris `UA = "KelasWebSemantik/1.0 (mahasiswa@usu.ac.id)"` dan `sp = SPARQLWrapper("https://dbpedia.org/sparql", agent=UA)`. |
| **2. LIMIT saat eksplorasi** | Dipenuhi dengan klausa `LIMIT 10` di akhir query untuk membatasi jumlah *solution* yang dievaluasi oleh endpoint Wikidata. | Tidak menggunakan `LIMIT` karena ruang pencarian sudah dipersempit secara spesifik pada satu sutradara (`dbo:director dbr:Christopher_Nolan`) yang hanya memiliki 16 film. |
| **3. Simpan, jangan ulangi** | Tidak relevan di dalam berkas query `.rq` karena penyimpanan berkas diatur pada sisi skrip atau unduhan manual. | Dipenuhi pada baris `g.serialize("film_nolan.ttl", format="turtle")` dan `lokal = Graph().parse("film_nolan.ttl")`, sehingga query lanjutan (`Q_TANPA_TANGGAL`) dijalankan secara lokal tanpa membebani DBpedia lagi. |
| **4. Jangkar jalur** | Dipenuhi pada pola `?kota wdt:P31/wdt:P279* wd:Q515` (serta `wdt:P17 wd:Q252`), di mana jalur `wdt:P279*` dijangkarkan secara eksplisit ke IRI kelas kota (`wd:Q515`). | Tidak menggunakan operator jalur berulang (`*` atau `+`), melainkan terpaut langsung ke jangkar IRI `dbr:Christopher_Nolan` dan `dbo:Film`. |

- **Versi `a_kota_limit.rq` yang melanggar Aturan 4 :**
  ```sparql
  CONSTRUCT {
    ?kota a ex:Kota ;
          ex:nama ?nama ;
          ex:populasi ?pop .
  }
  WHERE {
    ?kota wdt:P31/wdt:P279* ?kelas .
    ?kota wdt:P17 ?negara ;
          wdt:P1082 ?pop ;
          rdfs:label ?nama .
    FILTER(LANG(?nama) = "id")
  }
  LIMIT 10
### alsannya Mengapa versi tersebut jauh lebih mahal bagi endpoint Karena ujung kanan jalur wdt:P31/wdt:P279* dan properti negara diganti menjadi variabel bebas (?kelas dan ?negara) tanpa jangkar IRI (wd:Q515 dan wd:Q252). Mesin SPARQL tidak dapat melakukan pencarian terarah dari satu titik, melainkan harus menelusuri penutupan transitif (transitive closure) seluruh hierarki subkelas untuk jutaan entitas di seluruh Wikidata sebelum menerapkan filter, yang memicu ledakan kombinasi (combinatorial explosion) dan timeout.

### Diskusi 1 - Taksonomi berubah
Jika hasil materialisasi langsung digabungkan ke dalam graf produksi seperti pada kampus_v4.ttl (C1) lalu setahun kemudian taksonomi berubah—misalnya aturan ex:Mahasiswa rdfs:subClassOf foaf:Person atau ex:DosenTetap rdfs:subClassOf ex:Dosen dihapus maupun diubah—maka triple hasil inferensi lama yang kini menjadi salah (stale triples) adalah ex:andi a foaf:Person, ex:budi a ex:Dosen, ex:budi a foaf:Person, ex:rina a ex:Dosen, dan ex:rina a foaf:Person.

Masalah utamanya terlihat jelas saat kita membandingkan kampus_v4.ttl dari C1 dan kampus_turunan.ttl dari C2. Di dalam kampus_v4.ttl, 10 fakta eksplisit asli dan 6 fakta hasil inferensi telah melebur menjadi 16 triple tanpa penanda asal-usul (provenance). Sebagai contoh, pada blok ex:budi a ex:Dosen, ex:DosenTetap, foaf:Person, sistem tidak lagi bisa membedakan apakah ex:budi a ex:Dosen adalah fakta asli yang diinput manual ataukah murni hasil kesimpulan mesin. Untuk menemukan triple yang salah pada C1, kita terpaksa mengaudit dan membandingkan ulang seluruh graf produksi dengan berkas sumber kampus.ttl.

Sebaliknya, pendekatan C2 yang memisahkan 6 triple hasil inferensi ke dalam berkas tersendiri (kampus_turunan.ttl) menyelesaikan masalah ini secara tuntas. Saat taksonomi berubah, kita cukup menghapus atau mengosongkan kampus_turunan.ttl, memperbarui aturan rdfs:subClassOf pada kampus.ttl, lalu menjalankan ulang materialisasi_ulang.py untuk menghasilkan triple turunan baru yang bersih dan akurat.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk membangun dashboard populasi kota, query yang tepat adalah SELECT. Dashboard membutuhkan struktur data tabular (baris dan kolom) yang siap divisualisasikan langsung ke grafik atau tabel serta mendukung fungsi agregasi seperti MAX(?pop) atau SAMPLE(?pop) dengan GROUP BY ?kota. Berdasarkan temuan Bagian A pada query Wikidata, satu kota dapat memiliki beberapa klaim populasi historis sekaligus (fenomena populasi kembar), sehingga LIMIT 10 pada solution hanya menghasilkan 10 kota (30 triple), sedangkan tanpa penanganan agregasi, satu kota yang memiliki banyak nilai populasi akan mendominasi baris hasil dan menampilkan angka ganda pada dashboard. Dengan SELECT, duplikasi ini dapat diringkas langsung di tingkat query.

Sebaliknya, untuk menggabungkan data kota dari tiga sumber berbeda yang memakai kosakata berlainan, kita wajib menggunakan CONSTRUCT. Berbeda dengan SELECT yang hanya menghasilkan tabel datar, CONSTRUCT memetakan predikat yang beragam ke dalam satu skema target yang seragam dalam bentuk graf RDF baru yang siap disatukan (merge). Namun, temuan pada rusak_b.rq di Bagian D membuktikan bahwa penggabungan lintas sumber via CONSTRUCT memerlukan normalisasi nilai objek: ketika menggabungkan foaf:name, rdfs:label, dan schema:name, dbr:Christopher_Nolan menghasilkan 2 triple terpisah ("Christopher Nolan" dan "Christopher Nolan"@en) sehingga totalnya menjadi 4 triple, bukan 3. Dengan menambahkan normalisasi seperti BIND(STR(?n) AS ?nama) di dalam CONSTRUCT, barulah himpunan graf hasil otomatis mendeduplikasi nilai kembar lintas sumber menjadi tepat 3 triple yang bersih

## Cek Diri

| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | **Bagian A (Langkah 1 & Langkah 2 Soal C):** Pada Langkah 1, 4 *solution* × 2 pola template menghasilkan 8 cetakan triple, tetapi graf hasil akhir hanya menyimpan 6 triple karena `ex:tif2108 a ex:MataKuliahAktif` dan `ex:tif2104 a ex:MataKuliahAktif` yang tercetak dua kali digabung menjadi satu; begitu pula pada Langkah 2 Soal C, 4 baris *solution* (`ex:sari` muncul 2 kali) digabung oleh `CONSTRUCT` menjadi 3 triple. |
| 2 | **Bagian A (Langkah 2 Soal D), Bagian B (`demo_c.py`), dan Bagian D (`rusak_a.rq`):** Pada Soal D, `ex:rudi` tidak memiliki `ex:nama` sehingga variabel `?n` tak terikat (*unbound*) dan menghasilkan 0 triple tanpa error; pada Bagian B, 15 dari 16 film Nolan tidak memiliki `dbo:releaseDate` sehingga pola `schema:datePublished ?rilis` dilewati tanpa error (menghasilkan 49 triple); dan pada Bagian D, `rusak_a.rq` menghasilkan 0 triple tanpa error karena variabel `?film` di template tidak terikat. |
| 3 | **Bagian D (`rusak_b.rq` & `perbaikan_b.rq`):** Klausa `VALUES ?o { dbr:Christopher_Nolan dbr:Joko_Anwar dbr:Mira_Lesmana }` dikombinasikan dengan jalur alternatif `?o foaf:name\|rdfs:label\|schema:name ?n` berhasil menyatukan tiga predikat nama yang berbeda dari `film.ttl` ke dalam satu predikat target `ex:nama` (menghasilkan 4 triple sebelum normalisasi tag bahasa, dan 3 triple pada `perbaikan_b.rq`). |
| 4 | **Bagian A (Langkah 2 Soal A & B), Bagian C (`demo_d.py`), dan Bagian D (`perbaikan_c.rq`):** Jalur `?x a/rdfs:subClassOf* ex:Pegawai` (Soal B, 4 baris), `?x a/rdfs:subClassOf* ?super` (Bagian C, menurunkan `ex:budi a foaf:Person` dari `ex:DosenTetap` tanpa menyebut `ex:Dosen`), serta `?x a/rdfs:subClassOf* ex:Permukiman` pada `perbaikan_c.rq` (menemukan 3 permukiman: Medan, Surabaya, dan Tomok). |
| 5 | **Bagian C (`demo_d.py` vs `materialisasi_ulang.py`):** Pada `demo_d.py` (C1), setelah materialisasi awal menghasilkan 3 `foaf:Person`, penambahan data baru `ex:rina a ex:DosenTetap` membuat hasil query `Ada Rina` tetap bernilai 3; kesimpulan baru untuk Rina baru masuk setelah fungsi `materialisasi(g)` dihitung ulang pada Putaran 2 di `materialisasi_ulang.py` (C2), sehingga jumlah `foaf:Person` naik menjadi 4 dan total triple turunan menjadi 6. |
