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
Class: Pizza
Subclass: CheesyPizza
Individual: pizza:italy
Object property: pizza:hasTopping
Datatype property: Spiciness (hot, medium, mild)

## Layer Cake
Jelaskan posisi ontology dalam Semantic Web Layer Cake: [isi jawaban]

## Perbandingan serialisasi
- Turtle: [dua pengamatan sintaks]
- RDF/XML: [dua pengamatan sintaks]
- Kesamaan makna: [isi]

## Refleksi
1. Apa perbedaan ontology dan taksonomi?
   aksonomi hanya mengatur pengelompokan atau hierarki, sedangkan ontology menjelaskan pengelompokan sekaligus hubungan dan makna dari setiap data yang ada.
2. Mengapa domain pada OWL bukan constraint database?
3. Mengapa kosakata yang sudah ada sebaiknya dipakai kembali sebelum membuat yang baru?
