# Latihan Pertemuan 3 - JSON-LD dan Structured Data

## Identitas
- Nama: Aldiva Roelya Padang
- NIM: 251402007

## Struktur Hasil
- `profil_saya.jsonld`
- `profil_perbaikan.jsonld`
- `seminar.html`
- folder `screenshots`

## 1. JSON Biasa dan JSON-LD
1. Perbedaan fungsi kunci: kalo pada JSON biasa hanyalah nama atribut yang maknanya ditentukan oleh aplikasi yang menggunakannya, sedangkan pada JSON-LD memiliki makna yang sudah didefinisikan dalam kosakata Schema.org pada @context.
2. Fungsi `@context`, `@type`, dan `@id`: @context untuk menghubungkan stilah lokal ke kosakata atau standar global, jadinya arti data nya jelas
    sedangkan pada @type untuk menjelaskan atau menntekukan jenis entitas yang di jelaskan. pada soal adalah personh contohn nanusia atau seseorang. lalu @id untuk memberikann identitas unik untuk suatu entitas sehingga dapat di hubungkan dengan data lain yang ada di weeb semantik
3. Node tanpa `@id`: jika node tanpa @Id akan menjadi node anonim ataun node blank
   
## 2. Pemeriksaan schema.org
1. Alasan memilih tipe paling spesifik: Supaya data lebih jelas dan sesuai dengan jenis entitasnya. Contohnya, CollegeOrUniversity lebih tepat untuk universitas daripada hanya menggunakan Organization.
2. Nama properti dan bahasa nilai: Karena nama properti seperti name dan knowsAbout sudah menjadi standar dari Schema.org dan tidak boleh diganti. Sedangkan nilainya adalah isi data, jadi boleh menggunakan bahasa Indonesia.
3. Manfaat array pada `knowsAbout`: Array digunakan supaya satu orang bisa memiliki lebih dari satu pengetahuan sekaligus. Contohnya: ["Java", "Database", "Jaringan"].

## 3. Perbaikan Lima Kesalahan
| No. | Bagian Salah | Alasan | Perbaikan |
|---|---|---|---|
| 1 | "@type": "person" | pada schema.org person ditulis dengan awal kapital. | "@type": "Person" |
| 2 | 'name': "Rina Anggraini" | JSON hanya menggunakan tanda petik dua ("), jadi pada name tidak boleh memakai petik satu ('). | "name": "Rina Anggraini" |
| 3 | "birthDate": "12 September 2004" | Format tanggal tidak menggunakan standar ISO 8601. | "birthDate": "2004-09-12" |
| 4 | "nomorInduk": "221401001" | nomorInduk bukan properti yang sesuai pada Schema.org, Untuk menyimpan nomor identitas dapat menggunakan properti identifier. | "identifier": "221401001" |
| 5 | "identifier": "221401001", } | pada JSON tidak boleh ada koma setelah properti terakhir sebelum tanda }, jadi koma setelah properti terakhir harus di hapus. | "identifier": "221401001" } |

## 4. Triple dari JSON-LD Playground
Tuliskan satu baris N-Quads yang terbentuk:

```text
<https://usu.ac.id/mhs/251402043> <https://schema.org/name> "Gabriel Saurman Parhusip" .
```

## 5. Hasil Validasi
- Schema Markup Validator: Tidak ada kesalahan, tidak ada peringatan dan semuanya sudah benar sesuai dengan kosakata schema.org
- Rich Results Test: 1 item valid terdeteksi yakni 'Seminar Web Semantik'. Ada 8 masalah nontkritis hanyasaja opsional
- JSON-LD Playground: berhasil di expand menjadi 7 triple tanpa ada errror

## 6. Refleksi
1. Mengapa `@context` disebut jembatan menuju makna?: Karena @context memberi tau mesin arti dari istilah yang digunakan dalam JSON-LD. Jadi mesin tidak melihat teks saja, tetapi juga memahami maksud dari data tersebut.
2. Apa perbedaan fungsi Schema Markup Validator dan Rich Results Test?: Schema Markup Validator digunakan untuk mengecek apakah struktur dan penulisan Schema Markup sudah benar. Sedangkan Rich Results Test digunakan untuk melihat apakah data tersebut bisa mendukung tampilan khusus di hasil pencarian Google.
3. Mengapa isi JSON-LD harus sama dengan konten yang terlihat pada halaman?: Supaya informasi yang diberikan kepada search engine sesuai dengan informasi yang benar-benar dilihat oleh si pengguna. Kalau berbeda, data bisa dianggap tidak sesuai atau menyesatkan.

## Bukti
![Schema Markup Validator](screenshots/profil-schema-validator.png)
![JSON-LD Playground](screenshots/profil-playground.png)
![Rich Results Test](screenshots/seminar-rich-results.png)
