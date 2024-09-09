# SKIBISHOP
E-Commerce Web Application for True Sigma

### ⚙️ Tech Stack
- **Backend**: Django
- **Styling**: TailwindCSS CDN
- **Font**: Manrope
- **Web Service**: Pacil Web Service (PWS)

### 🪁 Deployment
Check out the live version here: [Skibishop Webpage](http://andrew-devito-skibishop.pbp.cs.ui.ac.id/)

---

## Tugas 2 - PBP 2024/2025

### 🛠️ Langkah Pengimplementasian

1. **Membuat sebuah proyek Django baru.**
   - Langkah pertama adalah inisialisasi proyek Django baru dengan perintah `django-admin startproject [nama_proyek]`. Ini akan membuat struktur direktori dasar yang dibutuhkan untuk proyek Django.

2. **Membuat aplikasi dengan nama main pada proyek tersebut.**
   - Setelah proyek dibuat, aplikasi dengan nama "main" harus ditambahkan menggunakan perintah `python manage.py startapp main`. Aplikasi ini akan berisi semua logika dan fitur yang akan dikembangkan.

3. **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
   - Dalam berkas `urls.py` proyek, tambahkan rute (route) untuk mengarahkan permintaan (request) ke aplikasi "main". Ini memastikan aplikasi "main" terhubung dan dapat dijalankan.

4. **Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**
   - Pada `models.py` di dalam aplikasi "main", buat model `Product` yang mewakili entitas produk. Model ini akan memiliki atribut yang wajib seperti `nama`, `deskripsi`, `harga`, dan sebagainya, yang akan digunakan untuk menyimpan data produk ke dalam database.

5. **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
   - Di `views.py`, buat fungsi yang akan merender template HTML. Template ini akan menampilkan informasi seperti nama aplikasi, nama kamu, dan kelas, yang akan diambil oleh fungsi tersebut.

6. **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
   - Di `urls.py` pada aplikasi "main", tambahkan rute baru yang akan memetakan URL ke fungsi di `views.py`. Hal ini memungkinkan pengguna untuk mengakses halaman yang telah dibuat melalui URL yang sesuai.

7. **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
   - Setelah aplikasi siap, lakukan deployment ke Pacil Web Service (PWS). Ini melibatkan mengunggah proyek ke server PWS sehingga aplikasi dapat diakses melalui Internet.

8. **Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.**
   - Terakhir, buat file `README.md` yang berisi deskripsi proyek, langkah-langkah implementasi, serta tautan menuju aplikasi yang sudah di-deploy di PWS. Sertakan juga jawaban untuk pertanyaan yang relevan tentang Django dan fungsionalitasnya.

### 🔄 Alur Django

### 🔧 Fungsi Git

Git berfungsi sebagai sistem kontrol versi (Version Control System) yang memungkinkan pengembang perangkat lunak untuk melacak setiap perubahan kode secara terperinci. Dengan Git, tim pengembang dapat bekerja secara kolaboratif pada proyek yang sama, mengelola cabang (branch) yang berbeda untuk fitur baru, memperbaiki bug, dan menggabungkan perubahan (merge) dengan aman. Git juga memungkinkan rollback ke versi sebelumnya jika terjadi kesalahan, sehingga meminimalisir risiko dalam pengembangan perangkat lunak. Dengan kata lain, Git membantu menjaga integritas kode dan memastikan tim dapat bekerja secara efisien dalam proyek yang kompleks.

### ❓ Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dijadikan framework pengenalan karena mendukung pengembangan cepat (rapid development) dan mengikuti praktik terbaik seperti arsitektur Model-View-Template (MVT). Kesederhanaannya memudahkan pemula untuk memahami konsep dasar seperti routing, templating, dan manajemen database tanpa terbebani oleh kode yang berlebihan. Selain itu, dokumentasi yang kuat dan komunitas yang besar membuatnya lebih mudah bagi pemula untuk mencari sumber belajar dan solusi.

### 💡 Mengapa model pada Django disebut ORM (Object-Relational Mapping)?

Model Django disebut ORM karena memungkinkan pemetaan objek Python ke dalam database relasional. Dengan ORM, pengembang dapat mengelola database menggunakan kode Python tanpa harus menulis kueri SQL secara langsung. ORM mengabstraksi interaksi dengan database, sehingga mempermudah pengelolaan data dan menjaga kode tetap konsisten dan mudah dipahami.
