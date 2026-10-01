# Pertemuan 6 - RDF Dasar


## RDF Triple

| Kalimat | Subject | Predicate | Object |
|----------|----------|----------|----------|
| Ida Adi adalah dosen. | ex:ida | rdf:type | ex:Lecturer |
| Ida Adi mengajar Web Semantik. | ex:ida | ex:teaches | ex:webSemantik |
| Mata kuliah itu memiliki nama "Web Semantik". | ex:webSemantik | ex:courseName | "Web Semantik" |


## IRI dasar graf


## Ringkasan graf
- Jumlah triple: 34 triple
- Namespace yang digunakan: ex, foaf, rdf dan xsd
- Entitas: 3 dosen, 2 mahasiswa, 3 mata kuliah

## Contoh triple
1. [subject] - [predicate] - [object]
2. [subject] - [predicate] - [object]
3. [subject] - [predicate] - [object]

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
3. Mengapa prefix membantu keterbacaan tanpa mengubah IRI?
   Prefix membuat IRI yang panjang menjadi lebih singkat dan mudah dibaca.
Contoh:
http://example.org/webSemantik → ex:webSemantik
Prefix hanya sebagai singkatan, jadi IRI yang dituju tetap sama.
5. Sebutkan satu kesalahan pemodelan yang Anda hindari pada graf ini.
