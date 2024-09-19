# SKIBISHOP
E-Commerce Web Application for True Sigma

### 🧑‍🦰 Author
- Name: Andrew Devito Aryo
- NPM: 2306152494
- Kelas: PBP F

### ⚙️ Tech Stack
- **Backend**: Django
- **Styling**: TailwindCSS CDN
- **Font**: Manrope
- **Web Service**: Pacil Web Service (PWS)

### 🪁 Deployment
Check out the live version here: [Skibishop Webpage](http://andrew-devito-skibishop.pbp.cs.ui.ac.id/)

### 📚 Archive Tugas
- [Tugas 2 PBP 2024/2025](https://github.com/Andrew4Coding/skibishop-pbp/wiki/Tugas-2-PBP-2024-2025)
- [Tugas 3 PBP 2024/2025](https://github.com/Andrew4Coding/skibishop-pbp/wiki/Tugas-3-PBP-2024-2025)

---

## Tugas 4 - PBP 2024/2025
### 1. Perbedaan antara `HttpResponseRedirect()` dan `redirect()`
- **`HttpResponseRedirect()`**:
  - Merupakan class bawaan Django yang mengembalikan respons HTTP 302 untuk melakukan redirect ke URL tertentu.
  - Biasanya digunakan ketika kita ingin memberikan lebih banyak kontrol dan modifikasi pada respon sebelum mengembalikannya.
  - Contoh: 
    ```python
    from django.http import HttpResponseRedirect
    
    def my_view(request):
        return HttpResponseRedirect('/some-url/')
    ```

- **`redirect()`**:
  - Merupakan shortcut function di Django yang secara internal menggunakan `HttpResponseRedirect()`.
  - `redirect()` lebih praktis karena bisa menerima berbagai parameter (URL, named URL patterns, model instances, dll.).
  - Contoh:
    ```python
    from django.shortcuts import redirect
    
    def my_view(request):
        return redirect('some-url-name')
    ```

**Perbedaan Utama**: `redirect()` adalah cara yang lebih sederhana untuk melakukan redirect dan fleksibel dalam hal parameter, sedangkan `HttpResponseRedirect()` memberi lebih banyak kontrol untuk modifikasi sebelum mengirimkan respons.

---

### 2. Cara Kerja Penghubungan Model `MoodEntry` dengan `User`
Dalam Django, model `MoodEntry` biasanya dihubungkan dengan model `User` menggunakan **ForeignKey**. Ini menghubungkan setiap `MoodEntry` ke pengguna tertentu yang telah login.

Contoh model `MoodEntry`:

```python
from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=50)
    entry_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.mood}"
```

- **Cara Kerja**:
  - Setiap kali pengguna membuat entri suasana hati, entri tersebut dikaitkan dengan `user` yang login.
  - **ForeignKey** digunakan untuk membuat relasi many-to-one antara `MoodEntry` dan `User`, di mana banyak entri bisa dimiliki oleh satu pengguna.
  - `on_delete=models.CASCADE` artinya jika pengguna dihapus, maka semua `MoodEntry` yang terkait juga akan dihapus.

---

### 3. Perbedaan antara Authentication dan Authorization
- **Authentication**: Proses verifikasi identitas pengguna (misalnya melalui username dan password). Ini adalah langkah pertama dalam memastikan bahwa pengguna adalah siapa yang mereka klaim.
  - Contoh: Saat pengguna login dengan username dan password, itu adalah proses otentikasi.

- **Authorization**: Proses memberikan izin kepada pengguna yang sudah diotentikasi untuk mengakses sumber daya tertentu berdasarkan hak akses yang dimiliki. 
  - Contoh: Setelah login, pengguna bisa diizinkan atau ditolak untuk mengakses halaman admin berdasarkan izin mereka.

**Proses Login Pengguna**:
- Saat pengguna login, **authentication** dilakukan untuk memastikan identitas mereka benar.
- Setelah berhasil, Django memberikan **authorization** dengan mengecek izin pengguna untuk melihat apakah mereka boleh mengakses sumber daya tertentu.

**Implementasi di Django**:
- Django menggunakan **middleware** untuk mengelola otentikasi dan otorisasi.
- Django menyimpan pengguna yang telah diotentikasi di objek request sebagai `request.user`.
- Untuk **authorization**, Django menggunakan **permissions** (izin) dan **groups** (kelompok), yang dapat diatur pada model atau view tertentu.

---

### 4. Bagaimana Django Mengingat Pengguna yang Telah Login
Django mengingat pengguna yang sudah login menggunakan **sessions** dan **cookies**.
- Setelah pengguna berhasil login, Django membuat session untuk pengguna dan menyimpan session ID dalam cookie di browser pengguna.
- Cookie ini kemudian dikirim ke server dengan setiap request berikutnya, memungkinkan Django untuk mengidentifikasi pengguna yang sudah login.

**Kegunaan Lain dari Cookies**:
- Cookies bisa digunakan untuk melacak preferensi pengguna, menyimpan keranjang belanja, atau menyimpan data sementara lainnya yang berguna di antara permintaan.
  
**Keamanan Cookies**:
- Tidak semua cookies aman. Misalnya, cookies yang tidak dilindungi bisa rentan terhadap serangan **Cross-Site Scripting (XSS)**.
- Untuk membuat cookies lebih aman, Django menawarkan beberapa opsi seperti:
  - **`HttpOnly`**: Mencegah cookie diakses melalui JavaScript.
  - **`Secure`**: Mengirim cookie hanya melalui HTTPS.

---

### 5. Step-by-Step Implementasi Checklist di Atas

1. **Membuat Model `MoodEntry` yang Terhubung ke `User`**:
   - Buat model dengan ForeignKey ke model `User` untuk menghubungkan setiap entri suasana hati ke pengguna tertentu.
   - Tambahkan field yang sesuai seperti `mood` dan `entry_date`.

   ```python
   from django.db import models
   from django.contrib.auth.models import User

   class MoodEntry(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       mood = models.CharField(max_length=50)
       entry_date = models.DateField(auto_now_add=True)
   ```

2. **Authentication dan Authorization**:
   - Gunakan Django’s authentication system untuk proses login, logout, dan pengelolaan izin akses pengguna.
   - Tambahkan permission-based authorization di view menggunakan `@login_required` atau `@permission_required` decorators untuk membatasi akses halaman.

   ```python
   from django.contrib.auth.decorators import login_required
   
   @login_required
   def my_view(request):
       # Hanya bisa diakses oleh pengguna yang login
       pass
   ```

3. **Implementasi Sessions dan Cookies**:
   - Django secara otomatis mengelola sessions dan menyimpan session ID di dalam cookies pengguna saat login.
   - Atur pengaturan keamanan cookie seperti `SESSION_COOKIE_SECURE = True` dan `SESSION_COOKIE_HTTPONLY = True` di settings.py untuk melindungi cookies.

4. **Mengimplementasikan Redirect dengan `redirect()`**:
   - Gunakan shortcut `redirect()` untuk mengarahkan pengguna setelah mereka berhasil login atau mengirimkan form.

   ```python
   from django.shortcuts import redirect
   
   def login_success(request):
       return redirect('dashboard')
   ```

---

# Langkah-langkah Implementasi Checklist
### 1. **Mengimplementasikan Fungsi Registrasi, Login, dan Logout**
- **Registrasi**:
   1. Buat form untuk pendaftaran pengguna baru menggunakan `UserCreationForm`.
   2. Buat view yang menangani form registrasi dan menyimpan pengguna baru ke database.
   3. Redirect pengguna ke halaman login setelah registrasi berhasil.

   **Langkah**:
   ```python
   from django.contrib.auth.forms import UserCreationForm
   from django.shortcuts import render, redirect

   def register(request):
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('login')
       else:
           form = UserCreationForm()
       return render(request, 'register.html', {'form': form})
   ```

   4. Buat template `register.html` untuk menampilkan form registrasi.

- **Login**:
   1. Gunakan Django’s built-in `LoginView` untuk menangani proses login.
   2. Sesuaikan URL ke `LoginView`.

   **Langkah**:
   ```python
   from django.contrib.auth.views import LoginView

   urlpatterns = [
       path('login/', LoginView.as_view(), name='login'),
   ]
   ```

- **Logout**:
   1. Gunakan Django’s `LogoutView` untuk menangani logout pengguna.
   2. Tambahkan URL logout di `urls.py` dan buat tautan logout pada template.

   **Langkah**:
   ```python
   from django.contrib.auth.views import LogoutView

   urlpatterns = [
       path('logout/', LogoutView.as_view(), name='logout'),
   ]
   ```

   3. Tambahkan link logout di template untuk memudahkan pengguna keluar:
   ```html
   <a href="{% url 'logout' %}">Logout</a>
   ```

---

### 2. **Membuat Dua Akun Pengguna dengan Dummy Data**
- **Langkah Membuat Akun Pengguna di Shell**:
   1. Buka shell Django: `python manage.py shell`
   2. Buat dua akun pengguna:
   ```python
   from django.contrib.auth.models import User
   user1 = User.objects.create_user('user1', 'user1@example.com', 'password123')
   user2 = User.objects.create_user('user2', 'user2@example.com', 'password123')
   ```

- **Langkah Menambahkan Dummy Data ke Model `MoodEntry`**:
   1. Gunakan shell Django untuk menambahkan tiga data dummy untuk setiap pengguna.
   ```python
   from myapp.models import MoodEntry
   MoodEntry.objects.create(user=user1, mood='Happy')
   MoodEntry.objects.create(user=user1, mood='Sad')
   MoodEntry.objects.create(user=user1, mood='Excited')

   MoodEntry.objects.create(user=user2, mood='Calm')
   MoodEntry.objects.create(user=user2, mood='Anxious')
   MoodEntry.objects.create(user=user2, mood='Neutral')
   ```

---

### 3. **Menghubungkan Model `Product` dengan `User`**
   - Buat model `Product` dan tambahkan ForeignKey ke `User`, sehingga setiap produk yang dibuat dapat dikaitkan dengan pengguna.

   **Langkah**:
   ```python
   from django.db import models
   from django.contrib.auth.models import User

   class Product(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       name = models.CharField(max_length=100)
       description = models.TextField()

       def __str__(self):
           return self.name
   ```

   - Jalankan migrasi untuk menerapkan perubahan:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

   - Tambahkan dummy data `Product` yang terhubung ke pengguna melalui shell:
   ```python
   from myapp.models import Product
   Product.objects.create(user=user1, name="Product A", description="Description of Product A")
   Product.objects.create(user=user2, name="Product B", description="Description of Product B")
   ```

---

### 4. **Menampilkan Detail Pengguna yang Sedang Login**
- Pada halaman utama (dashboard atau homepage), tampilkan detail informasi pengguna yang sedang login.

   **Langkah**:
   1. Pastikan bahwa view menggunakan `@login_required` untuk memastikan hanya pengguna yang sudah login yang bisa mengakses halaman tersebut.
   2. Di view, ambil data pengguna yang sedang login dengan `request.user`.

   ```python
   from django.contrib.auth.decorators import login_required
   from django.shortcuts import render

   @login_required
   def dashboard(request):
       return render(request, 'dashboard.html', {'user': request.user})
   ```

   3. Di template `dashboard.html`, tampilkan informasi pengguna:
   ```html
   <h2>Welcome, {{ user.username }}!</h2>
   ```

---

### 5. **Menerapkan Cookies untuk Last Login**
- Django secara otomatis menyimpan waktu terakhir pengguna login di field `last_login` di model `User`.

   **Langkah**:
   1. Di halaman utama, tampilkan `last_login` dari pengguna yang sedang login.
   2. Modifikasi view `dashboard` untuk menyertakan informasi `last_login` pengguna.

   ```python
   @login_required
   def dashboard(request):
       last_login = request.user.last_login
       return render(request, 'dashboard.html', {'user': request.user, 'last_login': last_login})
   ```

   3. Di template, tampilkan waktu login terakhir:
   ```html
   <p>Last login: {{ last_login }}</p>
   ```

### **Pengamanan Cookies**
   - Pastikan bahwa pengaturan session dan cookie aman di file `settings.py`:
   ```python
   SESSION_COOKIE_SECURE = True
   SESSION_COOKIE_HTTPONLY = True
   ```
