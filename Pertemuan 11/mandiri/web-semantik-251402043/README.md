# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

**Nama:** Gabriel Saurman Parhusip  
**NIM:** 251402043  

---

## Bagian A - LIMIT dan triple
- **Triple dengan LIMIT 10:** 30 triple
- **Triple dengan LIMIT 30:** 90 triple
- **Baris SELECT LIMIT 10 / kota berbeda:** 10 jumlah baris / 10 kota berbeda (`Jakarta`, `Muara Enim`, `Sekayu`, `Bangli`, `Baturaja`, `Amlapura`, `Banyuwangi`, `Tual`, `Soreang`, `Cikarang Pusat`)
- **Mengapa tidak (atau mengapa tepat) 30 triple:** 
  Hasil mencapai tepat 30 triple karena template CONSTRUCT memiliki tiga pola triple, yaitu `ex:Kota`, `rdfs:label`, dan `ex:populasi`. Dengan LIMIT 10, terdapat maksimal 10 solusi dari WHERE dan setiap solusi menghasilkan tiga triple. Berdasarkan hasil percobaan, seluruh triple yang dihasilkan berbeda sehingga tidak ada triple duplikat. Oleh karena itu, jumlah triple mencapai 10 × 3 = 30 triple.

## Bagian B - DBpedia ke Turtle
- **Output demo_c.py:** 48 triple, film tanpa tanggal: 16
- **Sumber data:** DBpedia (`https://dbpedia.org/sparql`)
- **Triple yang tetap tercetak untuk film tanpa tanggal:** `Triple schema:Movie`, `schema:name`, dan `schema:director tetap tercetak`. Sementara itu, `triple schema:datePublished` tidak tercetak karena film tidak memiliki informasi tanggal rilis. Hal ini tidak menyebabkan error karena bagian tanggal menggunakan OPTIONAL.
- **Query lokal tanpa internet:** Query kedua berhasil dijalankan tanpa internet karena graf sudah disimpan dalam file `film_nolan.ttl` dan dibaca kembali menggunakan Graph().parse(). Query dijalankan pada graf lokal menggunakan lokal.query(`Q_TANPA_TANGGAL`) tanpa mengirim permintaan baru ke endpoint DBpedia.
- **Mengapa dbo:Film memberi 0 pada film_nolan.ttl:** Karena template CONSTRUCT menggunakan tipe `schema:Movie`, bukan `dbo:Film`. Akibatnya, query yang mencari tipe `dbo:Film` tidak menemukan triple yang sesuai.

## Bagian C - Materialisasi
- **Output demo_d.py:** 
  ```text
  Sebelum: 0         
  Sesudah: 3
  Ada Rina: 3
  ```
- **Mengapa Ada Rina bernilai 3:** 
  Karena Rina ditambahkan sebagai ex:DosenTetap setelah proses materialisasi pertama selesai. Aturan inferensi belum dijalankan kembali, sehingga triple turunan untuk Rina belum terbentuk. Akibatnya, jumlah `foaf:Person` masih 3.
- **Output materialisasi_ulang.py:** 
  ```text
  Rina masuk | Person: 3
  Putaran 2 | Person: 4
  Triple turunan disimpan terpisah: 6
  ```
- **Tiga triple yang bukan baru:** 
  ex:budi a ex:DosenTetap
  ex:sari a ex:Dosen
  ex:andi a ex:Mahasiswa
  Ketiga triple tersebut sudah ada pada graf awal. Triple muncul kembali karena operator rdfs:subClassOf* memungkinkan jalur dengan panjang nol, sehingga tipe asli individu ikut dihasilkan oleh query CONSTRUCT.
- **Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa:** 
  File `kampus_turunan.ttl` digunakan untuk menyimpan triple hasil inferensi secara terpisah dari graf utama. Dengan pemisahan ini, hasil inferensi dapat diperiksa dan digunakan kembali tanpa mengubah data asli. Jika taksonomi kelas berubah, proses materialisasi harus dijalankan ulang secara manual agar triple turunan diperbarui sesuai hubungan subclass terbaru.

## Bagian D - Diagnosis

| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|---|---|---|---|---|
| `rusak_a.rq` | 0 triple | Graf kosong, tanpa error | Ketidakcocokan nama variabel antara template dan WHERE. Template menggunakan `?film` pada baris `CONSTRUCT { ?film ex:judul ?j . }`, sedangkan WHERE menggunakan `?f` pada baris `?f dbo:director dbr:Christopher_Nolan`, sehingga `?film` tidak terikat (*unbound*). | 3 triple (`dbr:Following`, `dbr:Insomnia`, dan `dbr:Memento`), masing-masing memiliki properti `ex:judul`. |
| `rusak_b.rq` | 4 triple | Dua nilai yang tampak sama | Pengambilan duplikasi literal nama dengan variasi bahasa. Pada baris `?o foaf:name\|rdfs:label\|schema:name ?n .`, `dbr:Christopher_Nolan` memiliki dua literal, yaitu `"Christopher Nolan"` (tanpa tag bahasa dari `foaf:name`) dan `"Christopher Nolan"@en` (dengan tag bahasa dari `rdfs:label`), sehingga RDF menganggap keduanya sebagai dua objek berbeda. | 3 triple, tepat satu `ex:nama` per orang setelah dinormalisasi menggunakan `BIND(STR(?n) AS ?nama)`. |
| `rusak_c.rq` | 0 triple | Superkelas tidak ditemukan | Pola tidak menelusuri hierarki taksonomi. Baris `?x a ex:Permukiman .` pada WHERE hanya mencari kecocokan kelas langsung, padahal entitas permukiman di `kota.ttl` bertipe subkelas turunan (`ex:KotaMetropolitan`, `ex:KotaDiIndonesia`, dan `ex:Desa`). | 3 triple (`ex:Medan`, `ex:Surabaya`, dan `ex:Tomok`) bertipe `ex:Permukiman` setelah menggunakan property path `a/rdfs:subClassOf*`. |

### E1. Etika Endpoint

| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak diatur dalam file `.rq` karena file ini hanya berisi query SPARQL, bukan kode yang mengirim permintaan HTTP. | Menggunakan User-Agent bermakna melalui variabel `UA = "KelasWebSemantik/1.0 (gabrielparhusip59@gmail.com)"` yang diteruskan ke `SPARQLWrapper` melalui `agent=UA`. |
| 2 LIMIT | Menggunakan `LIMIT 10` pada akhir query untuk membatasi jumlah hasil eksplorasi menjadi maksimal 10 solusi. | Tidak terlihat pengaturan LIMIT secara langsung pada `demo_c.py`. Query utama dibaca dari file `q_demo_b.rq`, sehingga penggunaan LIMIT perlu diperiksa pada file tersebut. |
| 3 Simpan, jangan ulangi | File `.rq` hanya menyimpan query, bukan hasil graf. Hasil query perlu disimpan agar tidak perlu mengambil data berulang kali dari endpoint. | Menyimpan hasil pengambilan data ke `film_nolan.ttl` menggunakan `g.serialize()`, kemudian membaca kembali file tersebut melalui `Graph().parse()` dan melakukan query secara lokal tanpa internet. |
| 4 Jangkar jalur | Menggunakan property path `wdt:P31/wdt:P279* wd:Q515`. Jalur memiliki titik acuan yang jelas, yaitu `wd:Q515`, sehingga pencarian dibatasi pada kelas kota dan turunannya. | Query `Q_TANPA_TANGGAL` tidak menggunakan property path. Query `Q_NOLAN_GRAF` berasal dari file `q_demo_b.rq`, sehingga penggunaan jangkar jalur perlu diperiksa pada file tersebut. |

**Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:**

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?x ?y
WHERE {
    ?x rdfs:subClassOf* ?y .
}
```

Query tersebut melanggar aturan jangkar jalur karena menggunakan dua variabel bebas, yaitu `?x` dan `?y`, tanpa IRI atau kelas tertentu sebagai titik acuan. Akibatnya, endpoint harus menelusuri banyak kemungkinan hubungan subclass. Hal ini dapat memperbesar ruang pencarian, meningkatkan beban pemrosesan, dan menyebabkan query berjalan lebih lambat atau mengalami timeout. Oleh karena itu, property path sebaiknya menggunakan IRI atau kelas tertentu sebagai jangkar agar pencarian lebih terarah.
```



### Diskusi 1 - Taksonomi berubah

Apabila hasil materialisasi Demo D disimpan ke dalam graf produksi, perubahan taksonomi di kemudian hari dapat menyebabkan beberapa triple hasil inferensi menjadi tidak sesuai lagi. Contohnya, pada data awal `kampus.ttl`, `ex:DosenTetap` merupakan subclass dari `ex:Dosen`, sedangkan `ex:Dosen` merupakan subclass dari `foaf:Person`. Dari hubungan tersebut, sistem dapat menghasilkan triple tambahan seperti `ex:budi a ex:Dosen` dan `ex:budi a foaf:Person`.

Jika hubungan subclass tersebut kemudian diubah atau dihapus, triple hasil inferensi yang sebelumnya tersimpan bisa menjadi tidak valid berdasarkan taksonomi terbaru. Untuk menemukannya, saya akan membandingkan `kampus_v4.ttl` dari C1 dengan `kampus_turunan.ttl` dari C2. `kampus_v4.ttl` berisi graf yang sudah mengalami materialisasi, sedangkan `kampus_turunan.ttl` menyimpan hasil inferensi secara terpisah.

Selanjutnya, saya akan memeriksa kembali triple hasil inferensi berdasarkan hubungan subclass yang terbaru. Triple yang tidak lagi dapat dibuktikan melalui taksonomi baru dapat dianggap sebagai triple usang. Oleh karena itu, materialisasi perlu dijalankan ulang setiap kali terjadi perubahan taksonomi. Hasil inferensi lama juga perlu dibandingkan dengan hasil terbaru agar triple yang sudah tidak relevan dapat diperbarui atau dihapus dari graf produksi.

### Diskusi 2 - SELECT atau CONSTRUCT

Menurut saya, SELECT lebih tepat digunakan untuk kebutuhan dashboard populasi kota karena hasilnya berupa baris data yang dapat langsung digunakan untuk menampilkan nama kota dan jumlah populasinya. Hasil SELECT juga lebih mudah diolah menjadi tabel, grafik, maupun visualisasi lainnya.

Berdasarkan hasil Bagian A, query SELECT dengan LIMIT 10 menghasilkan 10 baris yang mewakili 10 kota. Sementara itu, query CONSTRUCT dengan LIMIT 10 menghasilkan 30 triple karena setiap solusi menghasilkan tiga pola triple, yaitu tipe kota, label, dan populasi. Hal ini menunjukkan bahwa jumlah triple yang dihasilkan CONSTRUCT tidak selalu sama dengan jumlah solusi query.

Temuan dari `rusak_b.rq` juga menunjukkan bahwa literal dengan teks sama tetapi tag bahasa berbeda dapat dianggap sebagai objek RDF yang berbeda. Contohnya, `"Christopher Nolan"` dan `"Christopher Nolan"@en` menghasilkan dua objek yang berbeda sehingga jumlah triple menjadi empat, bukan tiga. Kondisi ini perlu diperhatikan ketika menggabungkan data dari beberapa sumber.

Dengan demikian, SELECT lebih sesuai untuk dashboard populasi karena data lebih mudah dibaca dan diolah. Sementara itu, CONSTRUCT lebih tepat digunakan apabila diperlukan pembentukan graf RDF baru dengan struktur tertentu.

### Cek diri

| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1. CONSTRUCT mencetak template sekali per solution dan menggabungkan triple kembar. | Bagian A: CONSTRUCT LIMIT 10 menghasilkan 30 triple karena setiap solusi menghasilkan tiga triple. |
| 2. Triple dengan variabel tak terikat tidak dicetak, tanpa error. | Bagian D: `rusak_a.rq` menghasilkan 0 triple karena variabel `?film` pada template tidak terikat dengan variabel `?f` pada WHERE. |
| 3. UNION, jalur `|`, dan VALUES menyatukan predikat berbeda. | Bagian D: `rusak_b.rq` menggunakan VALUES untuk menentukan tiga orang dan property path `|` untuk mengambil nama dari beberapa predikat. |
| 4. Jalur `+` dan `*` menelusuri hierarki tanpa menyebutkan turunannya. | Bagian C: penggunaan `rdfs:subClassOf*` menelusuri hierarki kelas sehingga kelas turunan dapat ditemukan tanpa disebutkan satu per satu. |
| 5. Materialisasi menyimpan kesimpulan, tetapi harus diulang. | Bagian C: setelah Rina ditambahkan, materialisasi perlu dijalankan kembali agar tipe turunan Rina ikut terbentuk. |
