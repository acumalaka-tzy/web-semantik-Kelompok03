# Jawaban XPath Berdasarkan Katalog Buku

1. Memilih semua elemen buku:
-> `//buku`

2. Memilih semua judul buku:
-> `//buku/judul`

3. Memilih buku pertama:
-> `//buku[1]`

4. Memilih semua buku yang mempunyai atribut ISBN:
-> `//buku[@isbn]`

5. Memilih buku dengan harga lebih dari 100000:
-> `//buku[harga>100000]`

6. Mengambil nilai teks dari seluruh elemen pengarang:
-> `//pengarang/text()`