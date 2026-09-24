# Pertemuan 5 - Ontology dan Arsitektur Web Semantik

## Ontology mini kampus
- IRI dasar: https://satu.usu.ac.id/mahasiswa
- Domain: satu.usu.ac.id

## Komponen ontology
| Komponen | Makna | Contoh Domain USU |
|---|---|---|
| Class | Konsep atau kelompok abstrak | Mahasiswa,mata kuliah,fakultas|
| Subclass | Class yang lebih khusus | MahasiswaTI subclass dari mahasiswa,Mahasiswailkom subclass dari mahasiswa |
| Individual | Instance konkret | Aldiva Roelya Padang bertipe mahasiswa, FASILKOM-TI bertipe fakultas |
| Property | Hubungan atau nilai | mengambil Mata kuliah, memiliki nim |
| Axiom | Aturan atau pernyataan | Mahasiswa belongs to some fakultas |

## pizza.owl
Class: Pizza |
Subclass: CheesyPizza |
Individual: pizza:italy |
Object property: pizza:hasTopping |
Datatype property: Spiciness (hot, medium, mild)

## Layer Cake
Jelaskan posisi ontology dalam Semantic Web Layer Cake: Ontology (OWL) posisinya tepat di atas RDF/RDFS dalam Layer Cake. Dia numpang di fondasi RDF (triple subjek-predikat-objek) dan RDFS (kosakata dasar kayak subClassOf, domain, range), terus nambahin logika yang lebih dalam, misalnya equivalentClass, disjointWith, cardinality, yang RDFS doang gak sanggup. Makanya ontology jadi dasar buat lapis-lapis di atasnya kayak SPARQL, Rules, Proof, sampai Trust. Sebelum data bisa di-query atau ditarik kesimpulan lewat reasoning, data itu harus udah dimodelin pakai ontology dulu. Jadi ontology bukan gantiin RDF, tapi bikin RDF "lebih paham konteks", dari cuma nyatet fakta jadi bisa dinalar sama mesin.

## Perbandingan serialisasi

- Turtle: Menggunakan deklarasi `@prefix` untuk mempersingkat penulisan URI dan menggunakan tanda titik (`.`) serta titik koma (`;`) untuk menuliskan triple secara ringkas.

- RDF/XML: Menggunakan struktur elemen XML dan deklarasi namespace seperti `xmlns:kampus`, dengan URI dituliskan melalui atribut `rdf:about` atau `rdf:resource`.

- Kesamaan makna: Kedua format merepresentasikan ontology mini Kampus yang sama, dengan class Mahasiswa, MataKuliah, dan Fakultas, subclass MahasiswaTI dan Mahasiswailkom, serta property mengambil, memilikiNIM, dan berasalDariFakultas. Individual Aldiva Roelya Padang dan FASILKOM-TI juga direpresentasikan dalam kedua format. Perbedaan keduanya hanya terletak pada bentuk sintaks serialisasi, bukan pada makna dan hubungan antarentitas.

## Refleksi
1. Apa perbedaan ontology dan taksonomi?
   aksonomi hanya mengatur pengelompokan atau hierarki, sedangkan ontology menjelaskan pengelompokan sekaligus hubungan dan makna dari setiap data yang ada.
2. Mengapa domain pada OWL bukan constraint database?
   Karena domain pada OWL hanya menunjukkan kelas atau jenis objek yang boleh memakai suatu properti, bukan aturan untuk membatasi data seperti pada database.
4. Mengapa kosakata yang sudah ada sebaiknya dipakai kembali sebelum membuat yang baru?
   Karena memakai kosakata yang sudah ada membuat data lebih mudah dipahami, konsisten, dan bisa terhubung dengan data dari sumber lain.
