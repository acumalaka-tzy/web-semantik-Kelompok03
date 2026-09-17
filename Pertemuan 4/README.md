# Pertemuan 4 — Metadata dan Interoperabilitas

## Identitas sumber
- Judul: Pengantar semantic web
- Pembuat: Dr. Anak gung Istri ngurah eka karyawati,S.Si.,M.eng
- URI sumber: https://id.scribd.com/document/536906501/b84bf491ca8b773ed40382f91a3ee8e
- Jenis sumber: Learning Resource
- Tanggal: 2017-06-17
- Deskripsi: Tentang pengatar web semantik untuk mahasiswa
- Bahasa: id
- Hak cipta: Hak Cipta penulis

  
## Pemetaan Dublin Core Terms
| Properti | Nilai | Alasan pemilihan |
| --- | --- | --- |
| dcterms:title | Pengantar Semantic Web | mengidentifikasi sumber secara jelas, wajib ada agar sumber dapat ditemukan dan dikenali |
| dcterms:creator | Dr. Anak Agung Istri Ngurah Eka Karyawati, S.Si., M.Eng | mencatat siapa penulis konten intelektual, disini yakni dosen pengajar |
| dcterms:description | 	Materi pengantar web semantik untuk mahasiswa | memberi konteks singkat tentang isi dan tujuan sumber, membantu pengguna menilai relevansi tanpa membuka dokumen penuh |
| dcterms:created | 	2017-06-17 | mencatat kapan konten dibuat, penting untuk menilai kemutakhiran materi (2017) |
| dcterms:type | 	Learning Resource | mengklasifikasikan sumber sebagai bahan belajar, bukan artikel berita atau dataset, sehingga membantu kategorisasi |
| dcterms:language | 	id] | menunjukkan bahasa penyajian (Indonesia/id), penting untuk pencarian dan aksesibilitas |
| dcterms:rights | 	Hak Cipta penulis | menyatakan status hak cipta, memberi kejelasan hukum tentang penggunaan ulang materi |
| dcterms:identifier | 	https://id.scribd.com/document/536906501/b84bf491ca8b773ed40382f91a3ee8e | menyediakan URI unik dan permanen ke lokasi sumber asli, memudahkan sitasi dan verifikasi |
| dcterms:publisher | Scribd | pihak yang menyediakan dan mempublikasikan akses ke dokumen ini secara online |

## Hasil validasi
- JSON-LD Playground: [ringkasan hasil]
- Schema Markup Validator: [ringkasan hasil]

## Refleksi
1. Mengapa URI yang sama penting untuk Turtle dan JSON-LD?
   -> Pakai URI yang sama itu penting supaya format Turtle dan JSON-LD menunjuk ke benda atau halaman yang persis sama. Jadi, sistem nggak menganggap itu dua data yang berbeda, melainkan satu sumber data yang utuh.  
3. Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?
   -> DC Terms dipakai untuk menjelaskan informasi dasar sumber, seperti judul, pembuat, dan tanggal. Sedangkan schema.org membantu mesin memahami isi data dengan lebih terstruktur.
4. Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.
   -> Data bisa salah dipahami oleh si mesin, misalnya judul di HTML berbeda dengan yang ada di JSON-LD, sehingga informasi menjadi tidak sesuai.

## Catatan akhir
[Tulis catatan singkat tentang konsistensi metadata Anda.]
