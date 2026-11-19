# Pertemuan 12 - Inferensi dan Reasoning

## Langkah 1 - Closure dengan tangan
| # | Triple turunan | Aturan | Premis |
|---|----------------|--------|--------|
| 1 | `ex:budi a ex:Dosen` | `rdfs2` | `ex:membimbing rdfs:domain ex:Dosen` + `ex:budi ex:membimbing ex:andi` |
| 2 | `ex:andi a ex:Mahasiswa` | `rdfs3` | `ex:membimbing rdfs:range ex:Mahasiswa` + `ex:budi ex:membimbing ex:andi` |
| 3 | `ex:budi ex:mengenal ex:andi` | `rdfs7` | `ex:membimbing rdfs:subPropertyOf ex:mengenal` + `ex:budi ex:membimbing ex:andi` |
| 4 | `ex:sari a ex:Dosen` | `rdfs9` | `ex:DosenTamu rdfs:subClassOf ex:Dosen` + `ex:sari a ex:DosenTamu` |
| 5 | `ex:DosenTamu rdfs:subClassOf ex:Pegawai` | `rdfs11` | `ex:DosenTamu rdfs:subClassOf ex:Dosen` + `ex:Dosen rdfs:subClassOf ex:Pegawai` |
| 6 | `ex:Dosen rdfs:subClassOf ex:Orang` | `rdfs11` | `ex:Dosen rdfs:subClassOf ex:Pegawai` + `ex:Pegawai rdfs:subClassOf ex:Orang` |
| 7 | `ex:budi a ex:Pegawai` | `rdfs9` | `ex:Dosen rdfs:subClassOf ex:Pegawai` + `ex:budi a ex:Dosen` (hasil #1) |
| 8 | `ex:andi a ex:Orang` | `rdfs9` | `ex:Mahasiswa rdfs:subClassOf ex:Orang` + `ex:andi a ex:Mahasiswa` (hasil #2) |
| 9 | `ex:sari a ex:Pegawai` | `rdfs9` | `ex:Dosen rdfs:subClassOf ex:Pegawai` + `ex:sari a ex:Dosen` (hasil #4) |
| 10 | `ex:DosenTamu rdfs:subClassOf ex:Orang` | `rdfs11` | `ex:DosenTamu rdfs:subClassOf ex:Pegawai` (hasil #5) + `ex:Pegawai rdfs:subClassOf ex:Orang` |
| 11 | `ex:budi a ex:Orang` | `rdfs9` | `ex:Dosen rdfs:subClassOf ex:Orang` (hasil #6) + `ex:budi a ex:Dosen` (hasil #1) |
| 12 | `ex:sari a ex:Orang` | `rdfs9` | `ex:Dosen rdfs:subClassOf ex:Orang` (hasil #6) + `ex:sari a ex:Dosen` (hasil #4) |

- Jumlah triple turunan bermakna: 12 triple (9 triple level instans/ABox dan 3 triple transitivitas `rdfs:subClassOf`/TBox).
- Triple yang baru ditemukan di putaran kedua: `ex:budi a ex:Pegawai`, `ex:andi a ex:Orang`, `ex:sari a ex:Pegawai`, `ex:DosenTamu rdfs:subClassOf ex:Orang`, `ex:budi a ex:Orang`, dan `ex:sari a ex:Orang` (ketika seluruh aturan dijalankan paralel per putaran; jika rantai `rdfs9` ditelusuri hanya memakai fakta `subClassOf` *asserted*, maka `ex:budi a ex:Orang` dan `ex:sari a ex:Orang` baru muncul pada putaran ketiga).
- Triple asserted yang tidak menurunkan apa pun, dan alasannya: `ex:andi a ex:MahasiswaBerprestasi`, karena kelas `ex:MahasiswaBerprestasi` tidak memiliki aksioma `rdfs:subClassOf` ke kelas mana pun (misalnya ke `ex:Mahasiswa`). Mesin RDFS memperlakukan IRI sebagai pengenal buram (*opaque identifier*) sehingga tidak dapat menyimpulkan hubungan dari kemiripan nama string.
## Langkah 2 - Tebak lalu cek
| Soal | Profil | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|--------|---------|-------------|-------------------------|
| A | RDFS | [isi] | [isi] | [isi] |
| B | OWL RL | [isi] | [isi] | [isi] |
| C | RDFS | [isi] | [isi] | [isi] |
| C | OWL RL | [isi] | [isi] | [isi] |
| D | OWL RL | [isi] | [isi] | [isi] |

## Langkah 3 - Reasoner pada graf kampus
- Berkas sumber dan IRI dasar graf: [isi]
- Asserted / closure / inferred / bermakna: [isi] / [isi] / [isi] / [isi]
- Triple di v4 yang tidak ada di asserted: [isi]
- Turunan yang muncul karena domain dan range ex:mengajar: [jawaban]
- Bila menambah dosen baru: [jawaban]

## Langkah 4 - Wikidata
- ?n Q8 / Q9: 877 / 1343
- Penyebab selisih: Penyebab utama selisih Q8 dan Q9 adalah adanya entitas yang termasuk instance dari subkelas universitas, tetapi tidak secara langsung memiliki tipe universitas (Q3918).
- Satu subkelas yang menyumbang selisih:  wd:Q845392 politeknik
- WDQS: materialisasi, saat query, atau tidak keduanya: Penalaran dilakukan saat query (query-time reasoning) secara eksplisit melalui property path P31/P279*, bukan melalui materialisasi inferensi permanen. WDQS menelusuri hubungan hierarki kelas ketika query dijalankan. Aturan RDFS9 direpresentasikan oleh pola query tersebut, bukan dijalankan secara otomatis oleh reasoner RDFS.

## Langkah 5 - Konsistensi
- Pesan galat RDFS / OWL RL: [isi] / [isi]
- Individu yang disebut pesan: [isi]
- Setelah baris terbalik dihapus: [isi]
- Isi laporan_kelas.csv sebelum dan sesudah: [isi]
- Dari mana dosen menjadi mata kuliah: [jawaban]

## Refleksi
1. Mengapa graf asserted disimpan terpisah dari graf inferred, dan apa akibatnya bila keduanya dicampur seperti kampus_usu_v4.ttl?
2. Pada Langkah 2, profil RDFS tidak memberi tahu bahwa aksioma OWL diabaikan. Bagaimana Anda akan memastikan profil yang dipakai sudah tepat untuk data Anda?
3. Kapan Anda memilih menulis jalur seperti wdt:P279* di query, dan kapan memilih menjalankan reasoner lalu menyimpan closure? 
Saya memilih menulis jalur seperti wdt:P279* di dalam query ketika kebutuhan penalarannya sederhana, hanya digunakan sesekali, dan ingin mendapatkan hasil secara langsung tanpa menyimpan hasil inferensi terlebih dahulu.

Sebaliknya, saya memilih menjalankan reasoner lalu menyimpan closure ketika data memiliki hierarki yang kompleks, aturan inferensi digunakan berulang kali, dan membutuhkan performa query yang lebih cepat.
