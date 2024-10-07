E-Commerce Web Application for True Sigma

### 🧑‍🦰 Author
- Name: Andrew Devito Aryo
- NPM: 2306152494
- Kelas: PBP F

### ⚙️ Tech Stack
- **Backend**: Django
- **Styling**: TailwindCSS CDN
- **Font**: Poppins
- **Web Service**: Pacil Web Service (PWS)

### 🪁 Deployment
Check out the live version here: [Skibishop Webpage](http://andrew-devito-skibishop.pbp.cs.ui.ac.id/)

### 📚 Archive Tugas
- [Tugas 2 PBP 2024/2025](https://github.com/Andrew4Coding/skibishop-pbp/wiki/Tugas-2-PBP-2024-2025)
- [Tugas 3 PBP 2024/2025](https://github.com/Andrew4Coding/skibishop-pbp/wiki/Tugas-3-PBP-2024-2025)
- [Tugas 4 PBP 2024/2025](https://github.com/Andrew4Coding/skibishop-pbp/wiki/Tugas-4-PBP-2024-2025)
---

## Tugas 6 - PBP 2024/2025
### 1. Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web
JavaScript adalah bahasa pemrograman yang sangat penting dalam pengembangan aplikasi web karena beberapa alasan berikut:
- **Interaktivitas Dinamis:** JavaScript memungkinkan pembuatan halaman web yang lebih interaktif, seperti animasi, tombol yang responsif, dan manipulasi elemen HTML tanpa perlu memuat ulang seluruh halaman.
- **Asynchronous Programming:** JavaScript mendukung asynchronous programming melalui penggunaan teknik seperti `AJAX` dan `fetch()`, yang memungkinkan data diambil dari server secara dinamis tanpa memengaruhi pengalaman pengguna.
- **Validasi Frontend:** JavaScript memungkinkan validasi input di sisi klien sebelum dikirimkan ke server, mengurangi jumlah kesalahan yang sampai ke backend.
- **Cross-Platform Compatibility:** JavaScript dapat digunakan di berbagai platform dan peramban, menjadikannya solusi fleksibel dan luas digunakan di berbagai perangkat.

### 2. Fungsi dari `await` pada `fetch()` dan Konsekuensinya Jika Tidak Digunakan
Fungsi `await` pada penggunaan `fetch()` berfungsi untuk menunggu penyelesaian dari `fetch` (operasi asynchronous) sebelum melanjutkan eksekusi baris kode selanjutnya. Ini memungkinkan kita mendapatkan data hasil respons sebelum digunakan lebih lanjut.

Jika kita **tidak menggunakan `await`**, maka program akan melanjutkan eksekusi tanpa menunggu hasil dari `fetch()`, yang menyebabkan:
- **Promise Pending:** Hasil dari `fetch()` akan berupa `Promise` yang belum selesai (pending), sehingga kita tidak bisa langsung menggunakan data hasil pengambilan tersebut.
- **Masalah Akses Data:** Variabel yang seharusnya menampung data hasil `fetch()` mungkin kosong atau belum berisi data, menyebabkan error atau perilaku yang tidak diinginkan di aplikasi.

### 3. Mengapa Menggunakan Decorator `csrf_exempt` pada View untuk AJAX POST
CSRF (Cross-Site Request Forgery) adalah mekanisme keamanan di Django yang memastikan permintaan POST berasal dari sumber yang sah. Namun, ketika menggunakan **AJAX POST**, permintaan ini sering kali tidak membawa token CSRF secara otomatis, sehingga bisa memicu kegagalan validasi CSRF.

Decorator `@csrf_exempt` digunakan untuk **menonaktifkan pengecekan CSRF pada view tertentu**. Ini bermanfaat pada situasi berikut:
- **Permintaan dari sumber terpercaya:** Misalnya, jika AJAX request berasal dari bagian aplikasi yang hanya bisa diakses oleh pengguna yang telah diverifikasi.
- **Mencegah kegagalan permintaan:** Tanpa decorator ini, AJAX POST tanpa token CSRF akan ditolak oleh Django.

Namun, penting untuk menggunakan decorator ini dengan hati-hati karena menonaktifkan mekanisme keamanan penting. Pastikan untuk tetap menjaga keamanan dengan memastikan bahwa hanya request yang aman yang dapat mencapai view ini.

### 4. Alasan Pembersihan Data Input Dilakukan di Backend, Bukan Hanya di Frontend
Pembersihan data input pengguna di backend tetap dilakukan meskipun sudah ada validasi di frontend karena beberapa alasan penting:
- **Keamanan:** Validasi dan pembersihan data di frontend dapat dilewati oleh pengguna yang memanipulasi request menggunakan alat seperti Postman atau dengan menonaktifkan JavaScript. Backend adalah tempat yang lebih aman untuk memverifikasi data input.
- **Integritas Data:** Backend bertanggung jawab untuk memastikan bahwa semua data yang masuk ke dalam sistem sesuai dengan aturan yang telah ditentukan. Jika hanya mengandalkan validasi frontend, data yang tidak valid bisa tetap masuk ke database.
- **Menangani Serangan:** Serangan seperti **injection** (misalnya, SQL injection atau XSS) dapat terjadi jika data tidak disanitasi dengan baik di backend. Validasi dan pembersihan input di backend sangat penting untuk mencegah eksploitasi tersebut.
