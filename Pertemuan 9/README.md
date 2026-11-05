# Pertemuan 9 - SPARQL Dasar: Tell & Ask dan Endpoint

## Langkah 1 - Tabel binding
| Tahap | ?dosen | ?mk | ?namaMK |
| :--- | :--- | :--- | :--- |
| Pola 1, baris 1 | `ex:budi` | `ex:tif2305` | – |
| Pola 1, baris 2 | `ex:sari` | `ex:tif2410` | – |
| Pola 1, baris 3 | `ex:sari` | `ex:tif2305` | – |
| Pola 2, baris 1 | – | `ex:tif2305` | `"Web Semantik"` |
| Pola 2, baris 2 | – | `ex:tif2410` | `"Data Mining"` |
| Hasil akhir (gabung ?mk), baris 1 | `ex:budi` | `ex:tif2305` | `"Web Semantik"` |
| Hasil akhir (gabung ?mk), baris 2 | `ex:sari` | `ex:tif2410` | `"Data Mining"` |
| Hasil akhir (gabung ?mk), baris 3 | `ex:sari` | `ex:tif2305` | `"Web Semantik"` |
- Jumlah baris hasil akhir: 3
- Peran ?mk: Sebagai variabel penghubung (*join key*) yang mencocokkan node mata kuliah antara Pola 1 dan Pola 2 di dalam blok `WHERE`, meskipun kolomnya disembunyikan pada hasil akhir karena tidak dicantumkan di klausa `SELECT`.

## Langkah 2 - ASK dan dunia terbuka
1. Hasil: FALSE, Hasil FALSE bukan berarti Budi pasti tidak mengajar TIF2410. Artinya, informasi tersebut belum tersedia atau belum dinyatakan di dalam graf. Dalam asumsi dunia terbuka, informasi yang tidak ditemukan belum tentu berarti salah.
2. Hasil: 5 baris, Baris dengan ?a sama dengan ?b tetap muncul karena query tidak memiliki kondisi yang membatasi kedua variabel agar berbeda.
3. Pola menghasilkan nol baris karena literal tanpa penanda bahasa berbeda dengan literal berpenanda bahasa @id.

## Langkah 3 - Query lokal
- IRI dasar graf: `https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#`
- Jumlah triple awal / akhir: 34 / 38
- Fakta yang ditambahkan: `ex:ida ex:mengajar ex:data_mining` (Muhammad Isa Dadi Hasibuan mengajar Data Mining), ditambah `ex:data_mining` bertipe `ex:Course`, `foaf:name "Data Mining"@id`, dan `ex:jumlahKredit 3`


## Langkah 4 - Wikidata
- Jumlah baris Q1 dengan wdt:P31: 20
- Jumlah baris Q1 dengan wdt:P31/wdt:P279*: 20
- Penjelasan perbedaan: Perbedaan kedua query terletak pada cakupan pencarian datanya. wdt:P31 hanya mencari universitas yang secara langsung memiliki tipe Universitas. Sementara itu, wdt:P31/wdt:P279* mencakup universitas beserta kelas turunannya (subclass), sehingga pencariannya lebih luas. Meskipun kedua query menghasilkan 20 baris, hal ini karena jumlah data yang ditampilkan dibatasi menggunakan LIMIT 20.

## Langkah 5 - Endpoint dari Python
- agent=UA: [isi]
- setReturnFormat(JSON): [isi]
- b.get("kotaLabel", {}): [isi]

## Refleksi
1. Di titik mana SPARQL berbeda dari SQL?
2. Kapan Anda memakai graf lokal (rdflib) dan kapan endpoint publik?
3. Sebutkan satu hasil query yang mengejutkan dan jelaskan penyebabnya.
