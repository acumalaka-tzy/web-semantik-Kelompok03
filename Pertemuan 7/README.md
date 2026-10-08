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
- Triple yang dianotasi: `ex:ida ex:mengajar ex:web_semantik`
- Creator: `ex:ida`
- Date: 2026-10-01
- Source: Data akademik kampus

## Perbandingan
- Format paling mudah dibaca manusia: [isi dan alasan]
- Format untuk HTML/API: [isi dan alasan]
- Perbedaan reifikasi klasik dan RDF-star: Reifikasi klasik lebih verbose karena RDF 1.1 tidak bisa menunjuk triple secara langsung, sehingga triple harus dibongkar menjadi resource `rdf:Statement` dengan empat triple pembungkus (type, subject, predicate, object) sebelum diberi anotasi. RDF-star menulis triple langsung sebagai subjek, `<< ex:ida ex:mengajar ex:web_semantik >> dct:creator ex:ida .`, jadi cukup satu pernyataan tanpa resource perantara. Reifikasi klasik lebih kompatibel dengan tool RDF 1.1, sedangkan RDF-star lebih ringkas tetapi butuh tool yang mendukungnya.

## Refleksi
1. Mengapa named graph berguna saat menggabungkan data dari sumber berbeda? -> Named graph berguna saat menggabungkan data dari sumber berbeda karena kita bisa membedakan data berdasarkan sumbernya. Jadi, kita tau data tertentu berasal dari sumber mana dan tidak bercampur begitu saja.
2. Mengapa provenance penting untuk sebuah triple? -> Provenance penting untuk sebuah triple karena kita bisa mengetahui asal-usul data tersebut, misalnya siapa yang membuat atau dari mana informasinya didapat. Dengan begitu, data lebih mudah dicek dan dipercaya.
3. Format apa yang Anda pilih untuk git diff, dan mengapa? -> Untuk git diff, kami memilih format Turtle (TTL) karena penulisannya lebih sederhana dan mudah dibaca. Perubahan data juga lebih gampang dilihat dibandingkan RDF/XML yang biasanya lebih panjang dan rumit.
