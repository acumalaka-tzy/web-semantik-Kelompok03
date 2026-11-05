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
- agent=UA: Digunakan untuk memberikan identitas aplikasi yang mengakses Wikidata. Identitas ini berupa User-Agent yang berisi nama aplikasi dan alamat email pengembang agar server dapat mengenali aplikasi yang mengirimkan permintaan data.
- setReturnFormat(JSON): Digunakan untuk menentukan format hasil respons dari SPARQL Endpoint, yaitu JSON. Format ini memudahkan Python dalam membaca dan mengolah data yang diperoleh dari Wikidata.
- b.get("kotaLabel", {}): Digunakan untuk mengambil nama kota dari hasil query SPARQL. Fungsi get() digunakan agar program tidak mengalami error apabila data kota tidak tersedia. Jika data tidak ditemukan, program akan memberikan nilai kosong ("").

## Refleksi
1. Di titik mana SPARQL berbeda dari SQL?
SPARQL dan SQL memiliki perbedaan pada cara mengakses dan mengolah data. SQL digunakan untuk mengambil data dari database relasional yang tersusun dalam tabel, baris, dan kolom. Sementara itu, SPARQL digunakan untuk mengambil data dari RDF yang direpresentasikan dalam bentuk graf dengan struktur Subject, Predicate, dan Object. SQL menggunakan perintah seperti SELECT, FROM, dan WHERE, sedangkan SPARQL menggunakan pola triple untuk mencari hubungan antar-data. Dengan demikian, SPARQL lebih berfokus pada hubungan dan keterkaitan antar-entitas.

2. Kapan Anda memakai graf lokal (rdflib) dan kapan endpoint publik?
Graf lokal menggunakan library RDFLib lebih cocok digunakan ketika ingin mengolah data RDF yang tersimpan secara lokal, melakukan pengujian query, atau mengembangkan aplikasi tanpa bergantung pada koneksi internet. Sementara itu, endpoint publik digunakan ketika membutuhkan data yang lebih luas dan tersedia secara online, seperti Wikidata. Endpoint publik memungkinkan pengguna mengambil informasi dari sumber data yang dapat diakses oleh banyak orang tanpa harus mengunduh seluruh dataset terlebih dahulu.

3. Sebutkan satu hasil query yang mengejutkan dan jelaskan penyebabnya.
Salah satu hal yang menarik dari hasil query Wikidata adalah terdapat universitas yang lokasi administratifnya tercatat di wilayah kabupaten, bukan hanya di kota. Hal ini cukup menarik karena nama universitas sering kali lebih dikenal berdasarkan nama kota besar di sekitarnya. Penyebabnya adalah Wikidata menyimpan informasi lokasi berdasarkan hubungan administratif yang tercatat dalam basis pengetahuannya. Oleh karena itu, hasil query dapat menunjukkan lokasi administratif yang lebih spesifik dibandingkan perkiraan berdasarkan nama universitas.