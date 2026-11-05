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
1. [jawaban]
2. [jawaban]
3. [jawaban]

## Langkah 3 - Query lokal
- IRI dasar graf: [isi]
- Jumlah triple awal / akhir: [isi] / [isi]
- Fakta yang ditambahkan: [isi]

## Langkah 4 - Wikidata
- Jumlah baris Q1 dengan wdt:P31: [isi]
- Jumlah baris Q1 dengan wdt:P31/wdt:P279*: [isi]
- Penjelasan perbedaan: [isi]

## Langkah 5 - Endpoint dari Python
- agent=UA: [isi]
- setReturnFormat(JSON): [isi]
- b.get("kotaLabel", {}): [isi]

## Refleksi
1. Di titik mana SPARQL berbeda dari SQL?
2. Kapan Anda memakai graf lokal (rdflib) dan kapan endpoint publik?
3. Sebutkan satu hasil query yang mengejutkan dan jelaskan penyebabnya.
