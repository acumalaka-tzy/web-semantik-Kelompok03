# Pertemuan 1 - Pengenalan Web Semantik

## 1. Eksplorasi Wikidata   
- Nama entitas: Universitas Sumatera Utara  
- Deskripsi entitas: Universitas di Indonesia  
- Identifier Wikidata yang diawali huruf Q: Q4200341  
- Negara: Indonesia  
- Lokasi: Jalan Dr T Mansur No 9 Padang Bulan  
- Tahun atau tanggal pendirian, jika tersedia: 4 Juli 1952   
- Website resmi: https://www.usu.ac.id/  
- Informasi lain yang menurut Anda menarik: Anggota dari Jaringan Universitas ASEAN dan juga ASEA-UNINET  

## 2. Entitas, Atribut, dan Relasi

| Informasi | Kategori | Alasan |
|---|---|---|
| Universitas Sumatera Utara | Entitas | Punya identitas sendiri sebagai sebuah lembaga dan dapat dibedakan dari universitas lain |
| Indonesia | Entitas | Punya identitas sendiri sebagai sebuah negara dan dapat dibedakan dari negara lain |
| Jaringan Universitas ASEAN | Entitas | Punya identitas sendiri sebagai organisasi/jaringan dan dapat dibedakan dari organisasi lain |
| ASEA-UNINET | Entitas | Identitas sendiri sebagai sebuah organisasi/jaringan universitas dan dapat dibedakan dari organisasi lain |
| Identifier Q4200341 | Atribut | Bukan objek yang berdiri sendiri, melainkan kode yang menjelaskan entitas USU di Wikidata |
| Deskripsi: universitas di Indonesia | Atribut | Informasi singkat yang menjelaskan apa itu entitas USU, bukan objek tersendiri |
| Alamat kampus: Jalan Dr. T. Mansur No. 9, Padang Bulan | Atribut | Nilai yang menjelaskan lokasi fisik entitas USU, bukan objek yang berdiri sendiri |
| Tahun pendirian: 4 Juli 1952 | Atribut | Tanggal yang menjelaskan kapan entitas USU didirikan, bukan objek tersendiri |
| Website resmi: https://www.usu.ac.id/ | Atribut | Tautan yang menjelaskan sarana informasi resmi entitas USU, bukan objek tersendiri |
| USU -> country -> Indonesia | Relasi | Menyatakan hubungan USU berada di negara Indonesia |
| USU -> member of -> Jaringan Universitas ASEAN | Relasi | Menyatakan hubungan keanggotaan antara entitas USU dengan entitas Jaringan Universitas ASEAN |
| USU -> member of -> ASEA-UNINET | Relasi | Menyatakan hubungan keanggotaan antara entitas USU dengan entitas ASEA-UNINET |

## 3. Eksplorasi Schema.org

| Property | Fungsi | Contoh Nilai |
|---|---|---|
| name | menyatakan nama universitas | Universitas Sumatera Utara |
| address | menyatakan alamat universitas | Jl. Dr. T. Mansur No. 9, Padang Bulan, Medan, Sumatera Utara, Indonesia |
| foundingDate | Menyatakan tanggal atau tahun berdirinya universitas | 1952-07-04 |
| url | Menyatakan alamat website universitas | https://www.usu.ac.id/ |
| logo | Menyatakan logo sebuah universitas | https://upload.wikimedia.org/wikipedia/commons/7/7a/University_of_north_sumatera_logo.jpg |
| email | Menyatakan email universitas | info@usu.ac.id |

## 4. Pertanyaan Evaluasi

### 1. Apa perbedaan web tradisional dan Web Semantik?
Jawaban: Perbedaan web semantik dengan traditional dapat dilihat dari siapa yang akan memproses dan memahami data.  jadi web traditional dibuat agar mudah dibaca dan dilihat oleh manusia sedangkan web semantik untuk data dan informasi dapat dipahami,diolah,serta dihubungkan secara otomatis oleh mesin atau komputer

### 2. Mengapa entitas membutuhkan identifier unik?
Jawaban: Entitas membutuhkan identifier unik agar setiap mahasiswa dapat dibedakan dengan jelas, meskipun ada mahasiswa yang memiliki nama yang sama. Misalnya, terdapat dua mahasiswa bernama “Andi”, maka keduanya dapat dibedakan menggunakan NIM seperti 231401001 dan 231401002. Dengan adanya identifier unik tersebut, sistem dapat mengetahui data, nilai, kelas, atau program studi yang dimiliki oleh masing-masing Andi tanpa tertukar. Jadi, identifier unik sangat penting untuk menghindari duplikasi dan kesalahan data serta memastikan setiap entitas dapat dikenali dan dihubungkan dengan tepat.

### 3. Jelaskan subject, predicate, dan object.
Jawaban:
- Subject merupakan entitas utama yang sedang dibahas atau dideskripsikan.
- Predicate merupakan hubungan, sifat, atau tindakan yang menjelaskan bagaimana subjek berelasi.
- Object merupakan suatu nilai, atribut atau entitas lain yang menjadi pelengkap atau tujuan dari predikat tersebut.

### 4. Apa keuntungan hubungan antarentitas?
Jawaban:
keuntungannya yaitu :
- Tidak buat ambigu, contohnya "java" di teks biasa itu berarti pulau, bahasa program, atau kopi. Jadi kalau direprentasikan sebagai entitas dengan identitas jelas (URL), mesin tidak salah paham.
- Mesin bisa nemuin fakta baru sendiri, misalnya mesin udag tau "Medan di Sumut" dan "Sumut di indonesia", mesin bisa menyimpulkan bahwa Medan itu di Indonesia, padahal belum ditulis.
- Langsung dapat jawaban, jika kita nyari sesuatu di google kadabng jawaban langsung muncul di kotak pencariannya.
- Gampang untuk diedit dan dilacak sumbernya, dengan menambahkan satu hubungan baru, kita bisa cek asalnya darimana.

### 5. Bagaimana Knowledge Graph membantu AI?
Jawaban:
knowledge graph membantu AI dengan cara membuat informasi lebih terstruktur dan saling terhubung. jadi, AI tidak hanya mengetahui sebuah informasi tetapi juga memahami konteks sebuah informasi dan dapat memahami hubungan antar informasi sehingga dapat membantu AI dalam penalaran dan memberikan jawaban yang akurat.
