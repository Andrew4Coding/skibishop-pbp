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

## Tugas 3 - PBP 2024/2025

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery memungkinkan komunikasi antara berbagai komponen dalam platform. Data delivery memastikan informasi dapat dikirimkan dengan aman, cepat, dan efisien dari satu titik ke titik lain, baik antar server, klien, maupun antar aplikasi. Tanpa mekanisme ini, platform tidak dapat berfungsi secara maksimal, karena data yang dibutuhkan untuk melakukan berbagai tugas tidak dapat dipertukarkan dengan benar.

---

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Secara umum, JSON lebih sering digunakan jika dibandingkan dengan XML untuk pengiriman data dalam pengembangan aplikasi modern. Alasannya adalah sebagai berikut:

- **Keringkasan**: JSON lebih ringkas dibandingkan XML, karena tidak memerlukan tag penutup yang berulang-ulang dan hanya dapat berbentuk array atau object. Hal ini membuat JSON lebih efisien dalam hal penyimpanan dan pengiriman data.
- **Kemudahan penggunaan**: JSON lebih mudah dibaca dan ditulis, baik oleh manusia maupun oleh mesin, karena menggunakan sintaks yang lebih sederhana.
- **Dukungan langsung dari JavaScript**: JSON secara alami terintegrasi dengan JavaScript, menjadikannya lebih mudah diimplementasikan dalam aplikasi web.

Walaupun XML menawarkan beberapa fitur tambahan seperti skema untuk validasi dan namespace, JSON lebih populer karena sifatnya yang lebih ringan dan mudah diimplementasikan, terutama dalam aplikasi web modern.

---

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang dimasukkan ke dalam form. Method ini mengecek apakah data yang di-submit oleh user sesuai dengan aturan validasi yang telah ditentukan di form (Misalnya form tidak kosong dan tidak melebihi maksimal karakter yang didefinisikan pada model Product). Jika data valid, method ini akan mengembalikan `True`, dan data tersebut bisa diproses lebih lanjut (misalnya, disimpan ke database). Jika data tidak valid, method ini mengembalikan `False` dan akan memberikan pesan error yang sesuai.

Tanpa method `is_valid()`, kita tidak bisa memastikan bahwa data yang masuk aman dan sesuai dengan aturan yang telah dibuat. Ini penting untuk menjaga integritas data dan keamanan aplikasi.

---

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` digunakan untuk melindungi aplikasi web dari serangan CSRF (Cross-Site Request Forgery). Serangan CSRF terjadi ketika seorang penyerang mengirimkan permintaan berbahaya ke server atas nama pengguna yang telah terautentikasi. 

Jika kita tidak menambahkan `csrf_token` pada form Django, penyerang dapat membuat skrip atau link yang secara otomatis mengirimkan request ke server kita dengan memanfaatkan kredensial pengguna yang sedang aktif. Tanpa token ini, server tidak dapat memverifikasi apakah permintaan yang diterima berasal dari sumber yang sah, sehingga memungkinkan penyerang untuk melakukan tindakan yang tidak diinginkan atas nama pengguna tersebut, seperti mengubah data atau melakukan transaksi tanpa izin.

---

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### 1. Membuat Input Form untuk Menambahkan Objek Model

**Langkah-langkah**:
1. **Buat Form di Django**: Buat form untuk model `Product` dengan menggunakan `ModelForm`.
    ```python
    from django.forms import ModelForm
    from main.models import Product
    
    class ProductEntryForm(ModelForm):
        class Meta:
            model = Product
            fields = ['name', 'price', 'description']
    ```

2. **Buat View untuk Input Form**: Buat view untuk menampilkan dan memproses form input.
    ```python
    def create_product_form(request):
        form = ProductEntryForm(request.POST or None)
    
        if form.is_valid():
            form.save()
            return redirect('main:show_model')
        
        context = {'form': form }
        return render(request, 'add/create_product.html', context)
    ```

3. **Buat Template HTML**: Buat template HTML untuk menampilkan form.
    ```html
    {% extends 'base.html' %} 
    {% block content %}
    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td>
            <input type="submit" value="Add Entry" class="bg-black w-fit py-3 px-10 text-white text-sm font-semibold rounded-[10px] hover:scale-105 duration-300"
            />
          </td>
        </tr>
      </table>
    </form>
    {% endblock %}
    ```

4. **Tambahkan URL Routing untuk Form**: Tambahkan URL untuk form di `urls.py`.
    ```python
    from django.urls import path
    from main.views import show_model, create_product_form, show_all_json, show_all_xml, show_id_json, show_id_xml
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_model, name='show_model'),
        path('add/', create_product_form, name='create_product_form'),
        # Endpoints lainnya
    ]
    ```

### 2. Menambahkan 4 Fungsi Views untuk Melihat Objek dalam Format XML dan JSON

**Langkah-langkah**:

1. **Buat View untuk Format JSON dan XML**:
    - **View untuk JSON**:
      ```python
      def show_all_json(_):
          data = Product.objects.all()
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```

    - **View untuk XML**:
      ```python
      def show_all_xml(_):
          data = Product.objects.all()
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```

    - **View untuk JSON by ID**:
      ```python
      def show_id_json(_, id: str):
          data = Product.objects.filter(id=id)
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
      ```

    - **View untuk XML by ID**:
      ```python
      def show_id_xml(_, id: str):
          data = Product.objects.filter(id=id)
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
      ```

2.  **Membuat Routing URL untuk Masing-masing View**
    Tambahkan URL routing untuk masing-masing views dalam format JSON dan XML ke dalam `urls.py`.
    ```python
    # urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', show_model, name='show_model'),
        path('add/', create_product_form, name='create_product_form'),
        path('xml/', show_all_xml, name='show_all_xml'),
        path('xml/<str:id>/', show_id_xml, name='show_id_xml'),
        path('json/', show_all_json, name='show_all_json'),
        path('json/<str:id>/', show_id_json, name='show_id_json'),
    ]
    ```

### Contoh Hasil API Call dengan Postman
**JSON All**
![image](https://github.com/user-attachments/assets/8a37fc24-443b-4d75-b53f-63d52425a348)

**XML All**
![image](https://github.com/user-attachments/assets/6f1998ca-70c7-4816-8875-4383b39c9452)

**JSON by ID**
![image](https://github.com/user-attachments/assets/46e4d308-dadf-4ce7-8774-476e75b1b066)

**XML by ID**
![image](https://github.com/user-attachments/assets/971b37b2-c5e6-4153-8713-d798f8a2a07e)
