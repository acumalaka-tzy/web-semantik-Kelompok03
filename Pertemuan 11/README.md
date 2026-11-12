# Pertemuan 11 - CONSTRUCT dan Hierarki Data

## Langkah 1 - Solution menjadi triple
| Solution | ?d | ?mk | Triple yang dicetak |
|----------|----|-----|---------------------|
| 1 | `ex:budi` | `ex:tif2108` | `ex:tif2108 a ex:MataKuliahAktif .`<br>`ex:tif2108 ex:diampuOleh ex:budi .` |
| 2 | `ex:budi` | `ex:tif2104` | `ex:tif2104 a ex:MataKuliahAktif .`<br>`ex:tif2104 ex:diampuOleh ex:budi .` |
| 3 | `ex:sari` | `ex:tif2108` | `ex:tif2108 a ex:MataKuliahAktif .`<br>`ex:tif2108 ex:diampuOleh ex:sari .` |
| 4 | `ex:ida` | `ex:tif2104` | `ex:tif2104 a ex:MataKuliahAktif .`<br>`ex:tif2104 ex:diampuOleh ex:ida .` |

- Jumlah solution: 4
- Jumlah cetakan triple: 8 (4 solution × 2 pola template)
- Jumlah triple di graf hasil: 6
- Triple yang tercetak lebih dari sekali:
  - `ex:tif2108 a ex:MataKuliahAktif .` (tercetak 2 kali, pada Solution 1 dan 3)
  - `ex:tif2104 a ex:MataKuliahAktif .` (tercetak 2 kali, pada Solution 2 dan 4)

## Langkah 2 - Tebak lalu cek
| Soal | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|---------|-------------|-------------------------|
| A | 2 baris | 3 baris | Operator property path `*` (zero or more) bersifat refleksif (mencocokkan jalur panjang 0), sehingga `ex:Dosen` ikut dihitung sebagai subkelas dari dirinya sendiri selain `ex:DosenTetap` dan `ex:DosenTamu`. |
| B | 3 baris | 4 baris (`ex:sari` muncul 2 kali) | `SELECT` tanpa `DISTINCT` mempertahankan multiset (duplikat baris), dan `ex:sari` memiliki dua jalur pencocokan yang valid ke `ex:Pegawai` (melalui `ex:DosenTetap` dan `ex:DosenTamu`). |
| C | 4 triple | 3 triple | Meskipun klausa `WHERE` menghasilkan 4 solution (dengan `ex:sari` dua kali), `CONSTRUCT` membentuk graf RDF yang merupakan himpunan (set), sehingga triple `ex:sari a ex:Pegawai` yang identik otomatis dideduplikasi menjadi satu. |
| D | 1 triple / Error | 0 triple (Tidak ada pesan error) | `ex:rudi` tidak memiliki properti `ex:nama` sehingga variabel `?n` berstatus *unbound* (kosong); aturan standar SPARQL `CONSTRUCT` secara otomatis mengabaikan pembuatan triple yang mengandung variabel *unbound* tanpa memicu error. |

## Langkah 3 - Graf kampus lokal
- Berkas sumber dan IRI dasar graf: `../Pertemuan 7/kampus_usu.ttl`; IRI dasar `https://zann-37.github.io/web-semantik-Kelompok03/251402110/kampus#`
- Kelas dosen dan properti nama: `ex:Lecturer` dan `foaf:name`
- Triple hasil pemetaan: 6 (3 dosen × 2 triple: `a schema:Person` dan `schema:name`)
- foaf:Person sebelum / sesudah: 0 / 3
- Triple asli vs turunan: Bisa dibedakan. Triple asli adalah yang saya tulis sendiri, yaitu data di `kampus_usu.ttl` (misal `ex:ida a ex:Lecturer`) dan dua pernyataan hierarki dari `INSERT DATA` (`ex:Lecturer rdfs:subClassOf ex:Pegawai` dan `ex:Pegawai rdfs:subClassOf foaf:Person`). Triple turunan adalah hasil materialisasi, sebanyak 6, yaitu `a ex:Pegawai` dan `a foaf:Person` untuk masing-masing dari 3 dosen (misalnya `ex:ida a foaf:Person`). Tidak ada satu pun yang saya ketik; semuanya dihitung dari hierarki `rdfs:subClassOf`. Setelah program selesai, keduanya sama-sama tertulis di `kampus_usu_v4.ttl`.
- Dosen baru setelah program selesai: Dosen baru tidak otomatis menjadi `foaf:Person`. Materialisasi hanya menghitung data yang ada saat query dijalankan, lalu hasilnya disimpan sebagai triple biasa. Jadi dosen yang ditambahkan sesudahnya hanya punya `a ex:Lecturer`, dan baru ikut menjadi `ex:Pegawai` dan `foaf:Person` jika program dijalankan ulang (atau jika memakai reasoner yang menghitung ulang otomatis).

## Langkah 4 - Wikidata
- Jumlah triple Q6: 144
- Jumlah baris Q6 versi SELECT: 50
- Penjelasan perbedaan: setiap baris SELECT akan menghasilkan tiga triple RDF, sehingga 50 baris seharusnya menghasilkan 150 triple. Namun, hasil CONSTRUCT hanya menghasilkan 144 triple. Perbedaan ini terjadi karena graf RDF tidak menyimpan triple yang duplikat. Apabila terdapat triple yang sama dari beberapa baris hasil SELECT, triple tersebut hanya dihitung satu kali. Dengan demikian, terdapat selisih 6 triple dari perhitungan teoritis.
- Q7 dengan + vs *: Operator + digunakan untuk mencari seluruh subkelas universitas yang memiliki minimal satu hubungan hierarki dengan kelas universitas (Q3918). Sementara itu, operator * digunakan untuk mencari subkelas dengan nol atau lebih hubungan hierarki. Dengan demikian, operator * juga dapat menampilkan kelas universitas itu sendiri (Q3918), sedangkan operator + hanya menampilkan kelas turunannya.
- Kelas yang mengejutkan dan alasannya: Kelas yang cukup mengejutkan adalah Coast Guard Academy (Akademi Penjaga Pantai). Kelas ini menarik karena merupakan institusi pendidikan yang memiliki fungsi khusus dalam melatih personel penjaga pantai. Kelas tersebut dapat menjadi subkelas universitas karena akademi ini termasuk lembaga pendidikan tinggi yang menyelenggarakan pendidikan dan pelatihan profesional pada bidang tertentu. Hal ini menunjukkan bahwa universitas tidak hanya mencakup institusi pendidikan umum, tetapi juga lembaga pendidikan khusus dengan bidang dan tujuan tertentu.

## Langkah 5 - Graf dari Python
- Jumlah triple universitas.ttl: [isi]
- Jumlah baris universitas_per_kota.csv: [isi]
- setReturnFormat(TURTLE): [isi]
- Graph().parse(data=...): [isi]
- Mengapa q_kota tidak memanggil endpoint: [isi]

## Refleksi
1. Mengapa jumlah triple hasil CONSTRUCT bisa lebih kecil dari jumlah baris SELECT dengan WHERE yang sama?
2. Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di kampus_usu_v4.ttl?
3. Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?
