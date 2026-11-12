# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

**Nama:** Yazri Khoiri Matondang  
**NIM:** 251402016  

---

## Bagian A - LIMIT dan triple

- **Triple dengan LIMIT 10:** 30 triple
- **Triple dengan LIMIT 30:** 90 triple
- **Baris SELECT LIMIT 10 / kota berbeda:** 10 baris / 10 kota unik (`Jakarta`, `Tubei`, `Turikale`, `Bondowoso`, `Tanah Merah`, `Kepanjen`, `Tanjung Selor`, `Sidoarjo`, `Kupang`, `Pekalongan`)
- **Mengapa tidak (atau mengapa tepat) 30 triple:**  
  Hasil eksekusi mencapai tepat 30 triple. Hal ini terjadi karena klausa `LIMIT 10` pada SPARQL membatasi jumlah *solution mappings* (baris pemenuhan kecocokan pola pada klausa `WHERE`), bukan membatasi jumlah triple RDF yang dihasilkan. Blok template `CONSTRUCT` memiliki 3 pola triple untuk setiap entitas:
  1. `?kota a ex:Kota`
  2. `?kota rdfs:label ?namaKota`
  3. `?kota ex:populasi ?populasi`  
  
  Berdasarkan inspeksi tabel `SELECT LIMIT 10`, ke-10 baris *solution* yang dikembalikan oleh Wikidata memiliki subjek `?kota` yang seluruhnya unik tanpa ada kota yang berulang dengan populasi ganda. Oleh sebab itu, 10 baris *solution* dikalikan dengan 3 pola template menghasilkan tepat $10 \times 3 = 30$ triple unik tanpa ada triple kembar yang tereliminasi oleh deduplikasi himpunan graf RDF.

---

## Bagian B - DBpedia ke Turtle

- **Output demo_c.py:** 48 triple, film tanpa tanggal: 16
- **Sumber data:** DBpedia (`https://dbpedia.org/sparql`)
- **Triple yang tetap tercetak untuk film tanpa tanggal:**  
  Triple yang tetap tercetak adalah `?film a schema:Movie`, `?film schema:name ?judul`, dan `?film schema:director dbr:Christopher_Nolan`. Sementara itu, triple `?film schema:datePublished ?rilis` tidak tercetak. Tidak ada pesan error yang muncul karena klausa `OPTIONAL { ?film dbo:releaseDate ?rilis }` mengizinkan variabel `?rilis` berstatus *unbound* (kosong) ketika data tanggal rilis tidak tersedia. Sesuai standar spesifikasi SPARQL `CONSTRUCT`, pola triple pada template yang mengandung variabel *unbound* akan secara otomatis dilewati (*silently omitted*) tanpa menggagalkan eksekusi query.
- **Query lokal tanpa internet:**  
  Menjalankan query `Q_TANPA_TANGGAL` saja secara lokal tetap berhasil karena query tersebut dievaluasi langsung oleh RDFLib pada berkas graf lokal `film_nolan.ttl` yang telah tersimpan di komputer, sehingga tidak memerlukan koneksi jaringan eksternal. Sebaliknya, bila seluruh skrip `demo_c.py` dijalankan ulang tanpa koneksi internet, program akan terhenti dengan pesan galat koneksi jaringan (`URLError` / `gaierror`) pada baris `sp.queryAndConvert()` saat mencoba menghubungi endpoint DBpedia jarak jauh.
- **Mengapa dbo:Film memberi 0 pada film_nolan.ttl:**  
  Karena pada query `q_demo_b.rq`, template `CONSTRUCT` menyelaraskan tipe kelas film dari DBpedia menjadi kosakata target Schema.org melalui konstruksi `?film a schema:Movie`. Akibatnya, kelas asli `dbo:Film` tidak pernah disertakan ke dalam graf serialisasi `film_nolan.ttl`. Sehingga, saat query kedua mencari entitas bertipe `dbo:Film`, graf lokal menghasilkan 0 kecocokan.

---

## Bagian C - Materialisasi

- **Output demo_d.py:**  
  ```text
  Sebelum: 0
  Sesudah: 3
  Ada Rina: 3
  ```
- **Mengapa Ada Rina bernilai 3:**  
  Karena proses inferensi melalui `CONSTRUCT` di RDFLib bersifat evaluasi satu kali (*one-shot evaluation*) saat perintah dipanggil, bukan merupakan *live inference engine* yang aktif terus-menerus di memori. Penambahan fakta baru (`ex:rina a ex:DosenTetap`) dilakukan setelah blok `CONSTRUCT` selesai dijalankan. Tanpa eksekusi inferensi ulang, fakta turunan bahwa Rina adalah `foaf:Person` belum dimaterialisasikan ke dalam graf `g`, sehingga query `Q_ORANG` tetap hanya menemukan 3 orang terdahulu (Budi, Sari, dan Andi).
- **Output materialisasi_ulang.py:**  
  ```text
  Putaran 1: 4 triple baru | Person: 3
  Rina masuk | Person: 3
  Putaran 2 | Person: 4
  Triple turunan disimpan terpisah: 6
  ```
- **Tiga triple yang bukan baru:**  
  Tiga triple tersebut adalah:
  1. `ex:budi a ex:DosenTetap`
  2. `ex:sari a ex:Dosen`
  3. `ex:andi a ex:Mahasiswa`  
  
  Ketiga triple ini dicetak oleh sifat refleksif langkah nol ($0\text{-length}$) pada operator properti `rdfs:subClassOf*`, di mana setiap kelas dianggap sebagai subkelas refleksif dari dirinya sendiri. Karena ketiga triple tipe kelas tersebut sudah dideklarasikan secara eksplisit di dalam `kampus.ttl` sejak awal, pengecekan `if t not in g` menyaring ketiganya sehingga tidak dihitung sebagai triple baru dan tidak dimasukkan ke graf turunan.
- **Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa:**  
  Kegunaan berkas terpisah `kampus_turunan.ttl` adalah memisahkan fakta turunan hasil inferensi (6 triple) dari fakta mentah dasar (`kampus.ttl`). Pendekatan ini menjaga silsilah data (*data provenance*), mempermudah audit, dan memungkinkan pembersihan instan bila aturan hierarki taksonomi berubah tanpa merusak basis data asli. Langkah manual yang tetap harus dilakukan adalah memanggil ulang fungsi `materialisasi(g)` setiap ada data baru, serta melakukan penghapusan dan materialisasi ulang dari nol apabila suatu kelas atau relasi subkelas lama dicabut, karena sistem tidak memiliki mekanisme *truth maintenance* otomatis untuk mencabut triple turunan basi.

---

## Bagian D - Diagnosis

| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|---|---|---|---|---|
| `rusak_a.rq` | 0 triple | Graf kosong, tanpa error | Ketidakcocokan nama variabel antara template dan WHERE: template menggunakan `?film` pada baris `CONSTRUCT { ?film ex:judul ?j . }`, sedangkan WHERE menggunakan `?f` pada baris `?f dbo:director dbr:Christopher_Nolan` sehingga `?film` tidak terikat (*unbound*). | 3 triple (`dbr:Following`, `dbr:Insomnia`, `dbr:Memento` masing-masing memiliki properti `ex:judul`). |
| `rusak_b.rq` | 4 triple | Dua nilai yang tampak sama | Pengambilan duplikasi literal nama dengan variasi bahasa: pada baris `?o foaf:name\|rdfs:label\|schema:name ?n .`, `dbr:Christopher_Nolan` memiliki dua literal yaitu `"Christopher Nolan"` (tanpa tag bahasa dari `foaf:name`) dan `"Christopher Nolan"@en` (dengan tag bahasa dari `rdfs:label`), sehingga RDF menganggapnya dua objek berbeda. | 3 triple (tepat satu `ex:nama` per orang setelah dinormalisasi menggunakan `BIND(STR(?n) AS ?nama)`). |
| `rusak_c.rq` | 0 triple | Superkelas tidak ditemukan | Pola tidak menelusuri hierarki taksonomi: baris `?x a ex:Permukiman .` pada WHERE hanya mencari kecocokan kelas langsung, padahal entitas permukiman di `kota.ttl` bertipe subkelas turunan (`ex:KotaMetropolitan`, `ex:KotaDiIndonesia`, `ex:Desa`). | 3 triple (`ex:Medan`, `ex:Surabaya`, dan `ex:Tomok` bertipe `ex:Permukiman` setelah menggunakan property path `a/rdfs:subClassOf*`). |

---

## Bagian E - Etika dan diskusi

### E1 - Etika Endpoint

| Aturan | a_kota_limit.rq | demo_c.py |
|---|---|---|
| **1. User-Agent bermakna** | Tidak relevan langsung pada teks berkas query `.rq` karena header HTTP diatur pada layer aplikasi klien/HTTP request. | Dipenuhi pada baris `UA = "KelasWebSemantik/1.0 (yazrikhoiri@students.usu.ac.id)"` yang dikirimkan melalui konfigurasi `SPARQLWrapper`. |
| **2. LIMIT saat eksplorasi** | Dipenuhi secara eksplisit dengan mencantumkan klausa `LIMIT 10` di akhir query untuk membatasi beban *solution mapping*. | Tidak menggunakan `LIMIT`, tetapi ruang pencarian query telah dipersempit dan diikat ke satu instan spesifik (`dbr:Christopher_Nolan`) yang hanya menghasilkan 16 entitas film. |
| **3. Simpan, jangan ulangi** | Tidak relevan langsung pada berkas query mentah `.rq`. | Dipenuhi dengan menyimpan graf hasil query ke berkas lokal `film_nolan.ttl` via `g.serialize()`, sehingga pemrosesan lanjutan dijalankan pada graf lokal tanpa query ulang ke DBpedia. |
| **4. Jangkar jalur** | Dipenuhi pada pola `?kota wdt:P31/wdt:P279* wd:Q515` di mana jalur penelusuran berulang dijangkarkan ke kelas kota `wd:Q515` dan negara `wd:Q252`. | Tidak relevan karena `q_demo_b.rq` tidak menggunakan operator property path berulang (`*` atau `+`). |

- **Versi yang melanggar aturan 4 (tidak dijalankan):**
  ```sparql
  # CONTOH PELANGGARAN ATURAN 4 (JANGAN DIJALANKAN)
  PREFIX ex: <http://contoh.id/>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX wdt: <http://www.wikidata.org/prop/direct/>

  CONSTRUCT {
    ?kota a ex:Kota ;
          rdfs:label ?namaKota ;
          ex:populasi ?populasi .
  }
  WHERE {
    ?kota wdt:P31/wdt:P279* ?kelasKota ;
          wdt:P17 ?negara ;
          wdt:P1082 ?populasi ;
          rdfs:label ?namaKota .
    FILTER ( LANG(?namaKota) = "id" )
  }
  LIMIT 10
  ```
- **Alasan mengapa versi tersebut jauh lebih mahal bagi endpoint:**  
  Pada versi pelanggaran di atas, ujung kanan operator jalur `wdt:P279*` diubah dari IRI konkrit `wd:Q515` menjadi variabel bebas tak terikat `?kelasKota`, serta entitas negara diubah menjadi variabel bebas `?negara`. Ketiadaan jangkar IRI tetap memaksa mesin SPARQL menghitung penutupan transitif (*transitive closure*) ke seluruh graf hierarki kelas di Wikidata tanpa batasan titik awal/akhir. Hal ini menimbulkan ledakan kombinatorial (*combinatorial explosion*), mengonsumsi memori dan CPU server secara masif, serta berujung pada kegagalan eksekusi (*timeout HTTP 500/504*).

---

### Diskusi 1 - Taksonomi berubah

Ketika hasil materialisasi digabungkan langsung ke dalam basis data produksi seperti pada implementasi `kampus_v4.ttl` (C1), seluruh triple hasil inferensi melebur tanpa jejak dengan triple fakta mentah awal. Jika setahun kemudian terjadi perubahan taksonomi—misalnya kebijakan institusi menghapus relasi `ex:Mahasiswa rdfs:subClassOf foaf:Person` atau mengubah `ex:DosenTetap` agar tidak lagi mewarisi `ex:Dosen`—maka triple turunan lama seperti `ex:andi a foaf:Person` dan `ex:budi a ex:Dosen` otomatis menjadi usang dan tidak valid (*stale triples*).

Masalah fatal pada pendekatan C1 adalah hilangnya informasi silsilah data (*data provenance*). Di dalam `kampus_v4.ttl`, sistem tidak memiliki metadata untuk membedakan apakah pernyataan `ex:budi a ex:Dosen` merupakan input eksplisit operator manusia atau sekadar kesimpulan otomatis mesin di masa lampau. Akibatnya, pelacakan dan penghapusan data basi menuntut audit manual menyeluruh dengan membandingkan basis data produksi terhadap dokumen sumber asli satu per satu.

Sebaliknya, arsitektur C2 yang menerapkan pemisahan triple turunan ke dalam berkas `kampus_turunan.ttl` memberikan solusi pemeliharaan yang bersih dan terisolasi. Jika taksonomi berubah, kita cukup mengosongkan berkas `kampus_turunan.ttl` tanpa menyentuh repositori data primer, lalu memperbarui berkas ontologi dasar dan mengeksekusi ulang `materialisasi_ulang.py`. Dengan demikian, graf inferensi yang baru langsung tergenerasi secara mutakhir, konsisten, dan bebas dari anomali data kadaluarsa.

---

### Diskusi 2 - SELECT atau CONSTRUCT

Untuk kebutuhan pembangunan dashboard analitik populasi kota, bentuk query yang paling tepat digunakan adalah **SELECT**. Dashboard aplikasi memerlukan struktur data tabular relasional (terdiri atas baris dan kolom) yang dapat langsung dipetakan ke komponen antarmuka pengguna seperti tabel, diagram batang, atau peta spasial. Selain itu, SELECT mendukung fungsi agregasi seperti `MAX(?populasi)` atau `SAMPLE(?populasi)` bersama klausa `GROUP BY ?kota`. Hal ini sangat krusial sebagaimana terbukti pada Bagian A, di mana data sensus populasi kota di Wikidata sering kali memiliki nilai ganda dari berbagai tahun pencatatan yang berbeda (fenomena populasi kembar). Dengan SELECT, kita dapat menyaring duplikasi angka tersebut di tingkat query agar visualisasi dashboard tidak menampilkan baris yang membingungkan.

Sebaliknya, untuk skenario integrasi data kota dari tiga sumber data independen yang mengadopsi kosakata dan skema ontologi berlainan, bentuk query yang wajib dipilih adalah **CONSTRUCT**. SELECT tidak mampu membentuk struktur graf pengetahuan baru, melainkan hanya menyajikan proyeksi nilai variabel. CONSTRUCT bertindak sebagai mesin transformasi (*data lifting & mapping*) yang memetakan beragam predikat lokal ke dalam skema kosakata target tunggal yang homogen.

Namun, pembelajaran dari kasus `rusak_b.rq` pada Bagian D membuktikan bahwa transformasi antar-sumber menggunakan CONSTRUCT tetap menuntut normalisasi data. Ketika menggabungkan properti nama dari berbagai sumber, variasi tag bahasa (seperti `"Christopher Nolan"` tanpa tag dan `"Christopher Nolan"@en`) akan membentuk dua triple RDF terpisah. Dengan menyisipkan fungsi penyeragaman seperti `BIND(STR(?n) AS ?nama)` di dalam blok CONSTRUCT, deduplikasi himpunan graf RDF bekerja secara optimal sehingga menghasilkan dataset gabungan yang rapi dan konsisten.

---

## Cek Diri

| No | Pernyataan | Bukti dari Tugas Ini |
|:---:|---|---|
| **1** | CONSTRUCT mencetak template sekali per solution dan menggabungkan triple kembar | **Bagian A (Langkah 1 & Langkah 2):** 10 baris *solution mapping* dari query Wikidata menghasilkan tepat 30 triple karena setiap baris mencetak 3 pola template dan semua subjek kota unik. Begitu juga pada pengujian `perbaikan_b.rq` di Bagian D, saat dua nilai literal Christopher Nolan dinormalisasi menjadi teks murni, CONSTRUCT secara otomatis menggabungkan duplikasi tersebut sehingga menghasilkan tepat 3 triple. |
| **2** | Triple dengan variabel tak terikat (*unbound*) tidak dicetak, tanpa error | **Bagian B (`demo_c.py`) & Bagian D (`rusak_a.rq`):** Pada `demo_c.py`, 16 film Nolan tidak memiliki data `dbo:releaseDate` sehingga variabel `?rilis` berstatus *unbound*; pola `schema:datePublished ?rilis` otomatis dilewati tanpa mencetak error (hanya mencetak 48 triple). Pada `rusak_a.rq`, variabel `?film` tidak terikat di WHERE sehingga menghasilkan 0 triple tanpa memicu kegagalan runtime. |
| **3** | UNION, jalur `\|`, dan VALUES menyatukan predikat berbeda | **Bagian D (`rusak_b.rq` & `perbaikan_b.rq`):** Penggunaan klausa `VALUES ?o { dbr:Christopher_Nolan dbr:Joko_Anwar dbr:Mira_Lesmana }` bersama properti alternatif `foaf:name\|rdfs:label\|schema:name` berhasil merangkum tiga predikat berbeda dari entitas berbeda menjadi satu predikat target `ex:nama`. |
| **4** | Jalur `+` dan `*` menelusuri hierarki tanpa menyebut perantara | **Bagian A (`a_kota_limit.rq`), Bagian C (`demo_d.py`), dan Bagian D (`perbaikan_c.rq`):** Pada `perbaikan_c.rq`, jalur `a/rdfs:subClassOf* ex:Permukiman` berhasil mengidentifikasi Medan, Surabaya, dan Tomok sebagai permukiman melalui kelas perantara (`ex:KotaMetropolitan`, `ex:KotaDiIndonesia`, `ex:Desa`) tanpa perlu mendefinisikan masing-masing subkelas perantara tersebut secara manual. |
| **5** | Materialisasi menyimpan kesimpulan, tetapi harus dihitung ulang | **Bagian C (`demo_d.py` vs `materialisasi_ulang.py`):** Pada `demo_d.py`, setelah materialisasi dilakukan, penambahan entitas Rina tidak mengubah jumlah orang (tetap 3). Kesimpulan baru bahwa Rina adalah `foaf:Person` baru tercipta setelah aturan inferensi dihitung ulang pada Putaran 2 di `materialisasi_ulang.py`, menaikkan jumlah person menjadi 4 dan total triple turunan menjadi 6. |

---

## 📸 Berkas Screenshot

Tiga screenshot tersimpan di folder `screenshots/`:
1. `screenshots/a-limit10.png` (Hasil eksekusi LIMIT 10 di Wikidata Query Service)
2. `screenshots/b-dbpedia.png` (Hasil eksekusi query Turtle di DBpedia SPARQL Endpoint)
3. `screenshots/c-materialisasi.png` (Terminal output eksekusi materialisasi ulang)

