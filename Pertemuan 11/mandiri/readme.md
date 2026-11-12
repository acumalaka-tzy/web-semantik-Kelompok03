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

## Bagian C - Materialisasi
- Output demo_d.py: [isi]
- Mengapa Ada Rina bernilai 3: [jawaban]
- Output materialisasi_ulang.py: [isi]
- Tiga triple yang bukan baru: [jawaban]
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: [jawaban]

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | [isi] | [isi] | [isi] | [isi] |
| rusak_b | [isi] | [isi] | [isi] | [isi] |
| rusak_c | [isi] | [isi] | [isi] | [isi] |

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
