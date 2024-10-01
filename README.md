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

## Tugas 5 - PBP 2024/2025
## 1. Urutan Prioritas CSS Selector
Ketika terdapat beberapa CSS selector yang diterapkan pada elemen HTML yang sama, CSS menggunakan aturan prioritas (specificity) untuk menentukan selector mana yang dipakai. Urutan prioritasnya adalah sebagai berikut:

1. **Inline Styles** (misalnya `style="color: red;"`) memiliki prioritas tertinggi.
2. **ID Selector** (misalnya `#header`) memiliki prioritas lebih tinggi dari class atau elemen.
3. **Class Selector** (misalnya `.menu`) lebih kuat daripada tag HTML.
4. **Tag Selector** (misalnya `h1`, `p`) memiliki prioritas terendah.
5. **Important Rule** (`!important`) dapat mengesampingkan semua urutan di atas dan memberikan prioritas tertinggi untuk suatu property.

### Contoh:
```html
<div id="header" class="menu">Title</div>
```

Jika terdapat CSS berikut:
```css
#header { color: blue; }
.menu { color: green; }
div { color: red; }
```
Maka elemen tersebut akan memiliki warna **biru** karena **ID selector** memiliki prioritas tertinggi.


## 2. Mengapa Responsive Design Penting?
**Responsive design** adalah pendekatan dalam desain web di mana tampilan halaman web dapat menyesuaikan diri dengan berbagai ukuran dan orientasi layar perangkat pengguna. Konsep ini penting karena pengguna mengakses web dari berbagai perangkat seperti komputer desktop, tablet, dan ponsel pintar.

### Keuntungan Responsive Design:
- Pengalaman pengguna yang lebih baik di berbagai perangkat.
- Aksesibilitas yang lebih luas.
- SEO lebih baik karena mesin pencari menghargai situs web yang ramah perangkat seluler.

### Contoh Aplikasi yang Sudah Menerapkan Responsive Design:
- **Google**: Halaman pencarian yang responsif di berbagai perangkat.
- **Airbnb**: Menyediakan pengalaman yang seragam di ponsel, tablet, dan desktop.

### Contoh Aplikasi yang Belum Menerapkan Responsive Design:
- **SIAK NG**: Hanya menyediakan tampilan yang rapih untuk mode desktop
    <div>
      <img src="https://github.com/user-attachments/assets/51cc32ba-94b9-490e-a80c-4ce23dfc384e" alt="Tampilan siak" width="400"/>
    </div>
---

## 3. Perbedaan antara Margin, Border, dan Padding
### 1. **Margin**: Ruang di luar elemen, antara elemen dengan elemen lainnya.
### 2. **Border**: Garis yang membungkus elemen, terletak di antara margin dan padding.
### 3. **Padding**: Ruang di dalam elemen, antara konten dan border.

### Cara Implementasi:
```css
div {
    margin: 20px;    /* Ruang luar elemen */
    border: 2px solid black;    /* Garis di sekitar elemen */
    padding: 10px;   /* Ruang dalam elemen */
}
```
### Ilustrasi:
<div>
  <img src="https://github.com/user-attachments/assets/e0572824-eaa3-4436-a48d-eba8d312d887" alt="css-box" width="400" />
</div>

---

## 4. Konsep Flexbox dan Grid Layout

### **Flexbox**
Flexbox (Flexible Box) adalah metode layout yang digunakan untuk mengatur elemen dalam satu dimensi, baik secara horizontal maupun vertikal. Flexbox memudahkan pembuatan layout yang fleksibel dan responsif.

#### Kegunaan Flexbox:
- Menyusun elemen secara dinamis dalam satu baris atau kolom.
- Memungkinkan elemen untuk diperluas atau diperkecil sesuai dengan ruang yang tersedia.

#### Contoh Penggunaan Flexbox:
```css
.container {
    display: flex;
    justify-content: center; /* Meletakan child element di tengah secara horizontal */
}
```

### **Grid Layout**
Grid Layout adalah sistem layout dua dimensi yang memungkinkan developer untuk membuat desain halaman yang lebih kompleks dengan baris dan kolom. Grid Layout sangat cocok untuk mengatur elemen dalam struktur grid agar rapih dan memiliki lebar kolom yang tetap.

#### Kegunaan Grid Layout:
- Membuat layout dua dimensi (baris dan kolom).
- Cocok untuk desain yang terstruktur dan memerlukan kedinamisan dalam mengatur lebar kolom dan barisnya.

#### Contoh Penggunaan Grid Layout:
```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr; /* Dua kolom, kolom kedua dua lebih besar 2 kali lipat dari yang kiri*/
    grid-gap: 10px; /* Jarak antar kolom */
}
```

---

# Langkah-langkah Implementasi Checklist
## Implementasi Fungsi Edit dan Hapus
### 1. **Buat view untuk Edit dan Delete**:
  ```python
  # View untuk menghapus produk
  def delete_product(request, id):
    # Mengambil produk yang memiliki id yang diinginkan**
    product = Product.objects.get(pk = id)

    # Menghapus produk sesuai dengan id yang dikirim
    product.delete()

    # Kembali ke halaman main
    return HttpResponseRedirect(reverse('main:show_main'))

  # View untuk mengedit produk
  def edit_product(request, id):
    # Mengambil produk yang memiliki id yang diinginkan
    product = Product.objects.get(pk = id)

    # Mengambil data produk dan mengirimkan nya ke form edit produ
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Jika form di submit, maka save dan kembali ke main
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    # Kirimkan data form ke template melalui context
    context = {
        'form': form, 
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "crud/edit_product.html", context)
  ```
### 2. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework
Sebelum memulai menggunakan Tailwind pada project, kita perlu menginisiasi pemanggilan Tailwind melalui CDN (Content Distribution Network). CDN memungkinkan untuk memakai fitur styling yang disediakan oleh Tailwind tanpa perlu mendownload atau mengkonfigurasi Tailwind pada direktori projek. CDN sendiri diletakkan pada `base.html`. Tailwind dipanggil dengan cara:
```html
  .....
        <script src="https://cdn.tailwindcss.com"></script>
        <script>
            tailwind.config = {
                theme: {
                        extend: {
                            fontFamily: {
                                'Manrope': ['Manrope', 'sans-serif'],
                                'Poppins': ['Poppins', 'sans-serif'],
                                'Inter': ['Inter', 'sans-serif'],
                            },
                    }
                }
            }
        </script>
    ....
```

Setelah menginisiasi Tailwind, ada beberapa component yang dikustomisasi designnya saat mengerjakan tugas ini, misalnya **Login, Register, Tambah Produk, Edit Produk, Daftar Produk, Card Product, dan lain-lain**. Berikut contoh implementasi untuk masing-masing component dapat diakses pada link-link berikut ini:
- [Login Page](https://github.com/Andrew4Coding/skibishop-pbp/blob/master/main/templates/auth/login.html)
- [Register Page](https://github.com/Andrew4Coding/skibishop-pbp/blob/master/main/templates/auth/register.html)
- [Create Product](https://github.com/Andrew4Coding/skibishop-pbp/blob/master/main/templates/crud/create_product.html)
- [Edit Product](https://github.com/Andrew4Coding/skibishop-pbp/blob/master/main/templates/crud/edit_product.html)
- [Tampilan Product](https://github.com/Andrew4Coding/skibishop-pbp/blob/master/main/templates/home/sections/products.html)
- [Card Product](https://github.com/Andrew4Coding/skibishop-pbp/blob/master/main/templates/home/elements/product.html)
- [Navigation Bar](https://github.com/Andrew4Coding/skibishop-pbp/blob/master/templates/components/navbar.html)

Semua kustomisasi dilakukan menggunakan TailwindCSS dan style dipanggil secara langsung dan inline melalui Tailwind CDN