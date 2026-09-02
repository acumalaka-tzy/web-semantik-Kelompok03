# Pertemuan 2 - Format Dokumen XML

## 1. Profil XML
Jelaskan secara singkat struktur XML yang Anda buat.  
struktur xml yang saya buat adalah isi tentang  biodata saya sebagai mahasiswa teknologi  informasi


## 2. Analisis Kesalahan XML

| No | Bagian yang Salah | Alasan | Perbaikan |
|---|---|---|---|
| 1 | ... | ... | ... |
| 2 | ... | ... | ... |
| 3 | ... | ... | ... |

## 3. Analisis XML Schema
1. Root element: buku
2. Tipe data judul: xs:string
3. Tipe data tahun: xs:gYear
4. Tipe data harga: xs:decimal
5. Atribut ISBN: atribut ISBN tidak boleh tidak ditulis karena terdapat use="required" yang dimana atribut tersebut wajib untuk ditulis

## 4. Analisis Namespace
1. Mengapa kedua elemen title tidak sama?:
   Karena walaupun sama-sama bernama title, keduanya berasal dari namespace yang berbeda. buku:title berasal dari namespace buku, sedangkan web:title berasal dari namespace web. Jadi XML menganggap keduanya sebagai dua elemen yang berbeda.
2. Fungsi prefix:
   Prefix buku: dan web: berfungsi sebagai penanda atau nama singkat untuk membedakan elemen. Jadi kita bisa tahu bahwa buku:title termasuk bagian dari namespace buku, sedangkan web:title termasuk bagian dari namespace web.
3. Fungsi xmlns:
   xmlns berfungsi untuk memberitahu XML bahwa prefix tertentu mengarah ke namespace tertentu. Contohnya xmlns:buku="https://example.org/buku" berarti prefix buku menggunakan namespace tersebut, begitu juga dengan prefix web.
4. Apakah URI namespace harus dapat dibuka?:
   Tidak harus. URI namespace hanya digunakan sebagai tanda pengenal supaya namespace bisa dibedakan satu sama lain. Jadi meskipun alamat tersebut tidak bisa dibuka di browser atau tidak memiliki halaman web, tetap bisa digunakan
   sebagai namespace.

## 5. Pertanyaan Evaluasi
1. Perbedaan XML dan HTML:  
Perbedaan nya adalah di XML kegunaan nya untuk transfer data sedangkan di HTML untuk penyajian data nya atau lebih tepatnya HTML dirancang untuk memfasilitasi transfer dokumen berbasis web atau bagaimana format tampilan dari data. Sedangkan XML lebih kepada struktur dan konteksnya

2. Apa yang dimaksud well-formed? ...

3. Perbedaan well-formed dan valid: ...

4. Mengapa XSD lebih kuat dibanding DTD? ...

5. Mengapa namespace penting? ...

6. Apa kegunaan XPath?  
Kegunaan XPath adaah sebagai alat navigasi untuk mencari dan memilih bagian tertentu dari sebuah dokumen XML (ataupun HTML)
