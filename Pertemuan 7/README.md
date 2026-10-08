# Pertemuan 7 - Serialisasi RDF

# Membandingkan Serialisasi RDF

| Format    | Kekuatan utama                           | Skenario tepat                                                                                                          |
| :-------- | :--------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| Turtle    | Ringkas dan mudah dibaca manusia         | Digunakan saat membuat atau mengedit data RDF secara manual karena sintaksnya sederhana dan mudah dipahami.             |
| JSON-LD   | Cocok web/API dan HTML                   | Digunakan untuk integrasi data RDF pada website, API, dan metadata HTML seperti Schema.org.                             |
| RDF/XML   | Kompatibilitas data lama                 | Digunakan ketika berinteraksi dengan sistem atau aplikasi lama yang masih menggunakan XML sebagai format utama.         |
| N-Triples | Satu triple per baris; stabil untuk diff | Digunakan untuk validasi, debugging, dan membandingkan perubahan data RDF menggunakan Git atau version control lainnya. |
| N-Quads   | Menambahkan konteks graf                 | Digunakan untuk menyimpan beberapa graph sekaligus dalam satu dataset RDF yang memiliki konteks atau sumber berbeda.    |

## Artefak
- Graf asal: [jumlah triple]
- Format ekspor: Turtle, JSON-LD, N-Triples
- Named graph: [nama graf 1] dan [nama graf 2]

## Reifikasi dan provenance
- Triple yang dianotasi: [isi]
- Creator: [isi]
- Date: [isi]
- Source: [isi]

## Perbandingan
- Format paling mudah dibaca manusia: [isi dan alasan]
- Format untuk HTML/API: [isi dan alasan]
- Perbedaan reifikasi klasik dan RDF-star: [isi]

## Refleksi
1. Mengapa named graph berguna saat menggabungkan data dari sumber berbeda?
2. Mengapa provenance penting untuk sebuah triple?
3. Format apa yang Anda pilih untuk git diff, dan mengapa?
