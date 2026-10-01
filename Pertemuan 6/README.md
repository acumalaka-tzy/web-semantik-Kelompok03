# Pertemuan 6 - RDF Dasar


## RDF Triple

| Kalimat | Subject | Predicate | Object |
|----------|----------|----------|----------|
| Ida Adi adalah dosen. | ex:ida | rdf:type | ex:Lecturer |
| Ida Adi mengajar Web Semantik. | ex:ida | ex:teaches | ex:webSemantik |
| Mata kuliah itu memiliki nama "Web Semantik". | ex:webSemantik | ex:courseName | "Web Semantik" |

1. Identifikasi jenis node untuk ex:ida, "Ida Adi"@id, dan [ ex:kota "Medan" ].
:  ex:ida adalah IRI (ditulis sebagai prefixed name), yaitu sumber daya dengan identitas global.
   "Ida Adi"@id adalah literal berupa string dengan language tag id (bahasa Indonesia).
   [ ex:kota "Medan" ] adalah blank node, yaitu node anonim tanpa IRI.

2. Mengapa literal tidak boleh menjadi subject RDF?
:  Subject harus berupa sumber daya yaitu IRI atau blank node yang bisa diidentifikasi dan dideskripsikan. Literal hanyalah nilai data seperti teks, angka, atau      tanggal, bukan entitas yang bisa diberi properti, sehingga literal hanya boleh menjadi object.

3. IRI dasar graf
https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#

4. Tuliskan kepanjangan namespace rdf, rdfs, xsd, dan foaf.
:  rdf  : Resource Description Framework (http://www.w3.org/1999/02/22-rdf-syntax-ns#)
   rdfs : RDF Schema (http://www.w3.org/2000/01/rdf-schema#)
   xsd  : XML Schema Definition (http://www.w3.org/2001/XMLSchema#)
   foaf : Friend of a Friend (http://xmlns.com/foaf/0.1/)

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
- Turtle: Penulisannya lebih singkat dan mudah dibaca karena menggunakan prefix seperti ex: dan foaf:. Hubungan antar-entitas juga terlihat lebih jelas.
- JSON-LD: Penulisannya lebih panjang karena menggunakan struktur JSON dan menampilkan IRI secara lengkap. Namun, format ini lebih mudah digunakan dalam aplikasi yang menggunakan JSON.
- Pernyataan yang sama: Kedua format menyimpan informasi RDF yang sama. Contohnya, pada Turtle: ex:ida ex:mengajar ex:web_semantik. Pada JSON-LD, pernyataan tersebut ditulis sebagai hubungan mengajar dari ida menuju web_semantik.

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
