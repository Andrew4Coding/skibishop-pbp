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
- [Tugas 5 PBP 2024/2025](https://github.com/Andrew4Coding/skibishop-pbp/wiki/Tugas-5-PBP-2024-2025)
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
- **Keamanan:** Validasi dan pembersihan data di frontend dapat dilewati oleh pengguna yang memanipulasi request menggunakan query-query atau dengan menonaktifkan JavaScript. Backend lebih aman dikarenakan data diproses secara lebih "tersembunyi" jika dibandingkan dengan diproses di frontend.
- **Integritas Data:** Backend bertanggung jawab untuk memastikan bahwa semua data yang masuk ke dalam sistem sesuai dengan aturan yang telah ditentukan. Jika hanya mengandalkan validasi frontend, data yang tidak valid bisa tetap masuk ke database. Misalnya, jika melakukan validasi nama yaitu hanya boleh 10 karakter melalui frontend (misalnya validasi form), timbul potensi serangan hacker yaitu dengan melakukan infiltrasi kepada API berupa mengirimkan nama dengan panjang 1000 karakter. Tentu hal ini bisa ditangani dengan baik jika diurus melalui database dan backend langsung.

## Langkah-langkah Implementasi Checklist yang Diterapkan

### 1. Mengubah Kode Kartu Data Produk agar Mendukung AJAX GET
Untuk mengubah metode GET menjadi AJAX, saya menambahkan view khusus pada `views.py` sebagai berikut:

```python
@csrf_exempt
@require_POST
def create_product_form_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    user = request.user
    
    new_product = Product(
        name=name,
        price=price,
        description=description,
        user=user
    )
    
    new_product.save()
    
    return HttpResponse(b"CREATED", status=201)
```

View ini akan dipanggil melalui *fetching* JavaScript, sehingga saya juga perlu menambahkan rute baru pada `urls.py`:

```python
path('create-ajax', create_product_form_ajax, name='create-ajax'),
```

Kemudian, saya memodifikasi tampilan HTML dengan menggantikan bagian yang sebelumnya memetakan produk dengan sebuah `div` ber-ID `product-container`. Div ini nantinya akan dimanipulasi menggunakan DOM melalui script JavaScript berikut:

```js
async function refreshProducts() {
    console.log("Refreshing products...");
    
    document.getElementById("product-container").innerHTML = "";

    const products = await getProducts();

    let htmlString = "";
    let classNameString = "";

    if (products.length === 0) {
        htmlString = "<p>No products found</p>";
    } else {
        classNameString = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10";
        products.forEach(product => {
            const name = DOMPurify.sanitize(product.fields.name);
            const price = DOMPurify.sanitize(product.fields.price);
            const pk = DOMPurify.sanitize(product.pk);

            htmlString += `
                <div class="rounded-3xl w-full md:w-[260px] border-[1px] border-black/10 shadow-xl p-5 text-black hover:shadow-xl cursor-pointer transition-all duration-300 flex flex-col gap-5">
                    <div class="w-full h-[200px] bg-[#F6F6F6] rounded-xl p-8 relative">
                        <img src="https://pngimg.com/d/macbook_PNG61.png" class="w-full object-contain h-full rounded-xl" />
                    </div>
                    <div class="flex flex-col">
                        <h3 class="m-0 font-medium text-sm">${name}</h3>
                        <h1 class="m-0 text-xl font-bold">Rp${price}</h1>
                        <h3 class="m-0 font-medium text-sm text-[#737373]">by AndrewStore</h3>
                        <h3 class="font-medium text-sm">4k Terjual</h3>
                        <div class="flex my-2 gap-2">
                            <a href='edit/${pk}' class="w-full">
                                <button class="bg-[#7C00FE] w-full py-3 px-5 text-white text-sm font-semibold rounded-3xl h-full hover:scale-105 duration-300">Edit</button>
                            </a>
                            <a href='delete/${pk}' class="w-full">
                                <button class="bg-[#D91656] w-full py-3 px-5 text-white text-sm font-semibold rounded-3xl h-full hover:scale-105 duration-300">Delete</button>
                            </a>
                        </div>
                    </div>
                </div>
            `;
        });
    }

    document.getElementById("product-container").className = classNameString;
    document.getElementById("product-container").innerHTML = htmlString;
}
```

Fungsi ini akan mengambil data produk secara asinkron dan memperbarui tampilan produk di halaman secara otomatis tanpa me-refresh halaman.

### 2. Mengambil Data Produk Milik Pengguna Tertentu Menggunakan AJAX GET
Agar data produk yang diambil melalui AJAX hanya milik pengguna yang sedang login, saya memastikan produk yang ditambahkan dikaitkan dengan pengguna tersebut pada view `create_product_form_ajax`:

```python
new_product = Product(
    name=name,
    price=price,
    description=description,
    user=request.user  # Pastikan hanya produk milik pengguna ditampilkan
)
```

### 3. Membuat Tombol untuk Membuka Modal dengan Form Tambah Produk
Langkah berikutnya adalah membuat tombol yang saat diklik akan membuka modal. Tombol ini diletakkan di dalam file `products.html`:

```html
<button
    data-modal-target="crudModal"
    data-modal-toggle="crudModal"
    class="bg-[#7C00FE] w-fit py-3 px-10 text-white text-sm font-semibold rounded-3xl h-full hover:scale-105 duration-300"
    onclick="showModal();"
>
    + Create (AJAX)
</button>
```

HTML untuk modal diletakkan dalam file terpisah `create_product_modal.html`, dan dimasukkan melalui `include` di file `product.html`. Berikut adalah logika untuk membuka dan menutup modal:

```js
function showModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modal.classList.remove('hidden');
    setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
    }, 50);
}

function hideModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    modalContent.classList.remove('opacity-100', 'scale-100');
    modalContent.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
        modal.classList.add('hidden');
    }, 150);
}

document.getElementById("cancelButton").addEventListener("click", hideModal);
document.getElementById("closeModalBtn").addEventListener("click", hideModal);

document.getElementById("submitProductEntry").onclick = addProduct;
```

Fungsi `showModal()` akan menampilkan modal, sedangkan `hideModal()` menutup modal. Saya juga menambahkan logika agar modal ditutup saat tombol cancel atau close diklik.

### 4. Membuat Fungsi View untuk Menambahkan Produk Baru ke Database
Fungsi untuk menambahkan produk baru sudah diimplementasikan pada langkah pertama menggunakan `create_product_form_ajax`.

### 5. Membuat Path /create-ajax/ untuk Fungsi View Baru
Path untuk view yang baru sudah ditambahkan di `urls.py` seperti yang dijelaskan di langkah pertama.

### 6. Menghubungkan Form di Modal dengan Path /create-ajax/
Form di dalam modal akan dihubungkan ke path `/create-ajax/` melalui fungsi `addProduct()` menggunakan `fetch()`.

### 7. Melakukan Refresh Tampilan Produk Secara Asinkronus Tanpa Reload Halaman
Setelah produk baru ditambahkan, tampilan daftar produk akan diperbarui secara otomatis tanpa memerlukan *reload* halaman, karena pengambilan data produk dilakukan secara asinkronus menggunakan AJAX.
