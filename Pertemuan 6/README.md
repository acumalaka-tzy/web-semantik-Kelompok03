# Pertemuan 6 - RDF Dasar


## RDF Triple

| Kalimat | Subject | Predicate | Object |
|----------|----------|----------|----------|
| Ida Adi adalah dosen. | ex:ida | rdf:type | ex:Lecturer |
| Ida Adi mengajar Web Semantik. | ex:ida | ex:teaches | ex:webSemantik |
| Mata kuliah itu memiliki nama "Web Semantik". | ex:webSemantik | ex:courseName | "Web Semantik" |


## IRI dasar graf
https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#


## Ringkasan graf
- Jumlah triple: 34 triple
- Namespace yang digunakan: ex, foaf, rdf dan xsd
- Entitas:
3 Dosen : Muhammad Isa Dadi Hasibuan, Dedy Arisandi, Ivan Jaya
3 Mata Kuliah : Web Semantik, Manajemen Basis Data, Pemrograman Web
2 Mahasiswa : Muhammad Izyan, Yazri Khoiri
1 Fakultas : Fakultas Ilmu Komputer dan Teknologi Informasi

## Contoh triple
1. EX.ida - RDF.type - EX.Lecturer
2. EX.ida - FOAF.name - "Muhammad Isa Dadi Hasibuan"
3. EX.ida - EX.mengajar - EX.web_semantik

## Perbandingan serialisasi
- Turtle: [pengamatan]
- JSON-LD: [pengamatan]
- Pernyataan yang sama: [isi]

## Refleksi
1. Kapan object harus berupa IRI dan kapan berupa literal?
   Object berupa IRI jika menunjuk ke suatu entitas yang masih bisa memiliki informasi lain, misalnya mata kuliah.
Contoh:
ex:ida ex:teaches ex:webSemantik
Literal digunakan untuk nilai langsung seperti teks, angka, atau tanggal.
Contoh:
ex:webSemantik ex:courseName "Web Semantik"
2. Mengapa prefix membantu keterbacaan tanpa mengubah IRI?
   Prefix membuat IRI yang panjang menjadi lebih singkat dan mudah dibaca.
Contoh:
http://example.org/webSemantik → ex:webSemantik
Prefix hanya sebagai singkatan, jadi IRI yang dituju tetap sama.
3. Sebutkan satu kesalahan pemodelan yang Anda hindari pada graf ini.
Kesalahan yang dihindari adalah menggunakan string sebagai object pada relasi mengajar.
