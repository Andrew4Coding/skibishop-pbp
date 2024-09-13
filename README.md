# SKIBISHOP
E-Commerce Web Application for True Sigma

### 🧑‍🦰 Author
- Name      : Andrew Devito Aryo
- NPM       : 2306152494
- Kelas     : PBP F

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

Data delivery penting karena memungkinkan komunikasi antara berbagai komponen dalam platform. Data delivery memastikan bahwa informasi dapat dikirimkan dengan aman, cepat, dan efisien dari satu titik ke titik lain, baik antar server, klien, maupun antar aplikasi. Tanpa mekanisme ini, platform tidak dapat berfungsi secara maksimal, karena data yang dibutuhkan untuk melakukan berbagai tugas tidak dapat dipertukarkan dengan benar.

---

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Secara umum, JSON lebih disukai dibandingkan XML untuk pengiriman data dalam pengembangan aplikasi modern. Alasannya adalah sebagai berikut:

- **Keringkasan**: JSON lebih ringkas dibandingkan XML, karena tidak memerlukan tag penutup yang berulang-ulang. Hal ini membuat JSON lebih efisien dalam hal penyimpanan dan pengiriman data.
- **Kemudahan penggunaan**: JSON lebih mudah dibaca dan ditulis, baik oleh manusia maupun oleh mesin, karena menggunakan sintaks yang lebih sederhana.
- **Dukungan langsung dari JavaScript**: JSON secara alami terintegrasi dengan JavaScript, menjadikannya lebih mudah diimplementasikan dalam aplikasi web.

Walaupun XML menawarkan beberapa fitur tambahan seperti skema untuk validasi dan namespace, JSON lebih populer karena sifatnya yang lebih ringan dan mudah diimplementasikan, terutama dalam aplikasi web modern.

---

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django digunakan untuk memvalidasi data yang dimasukkan ke dalam form. Method ini mengecek apakah data yang di-submit oleh user sesuai dengan aturan validasi yang telah ditentukan di form. Jika data valid, method ini akan mengembalikan `True`, dan data tersebut bisa diproses lebih lanjut (misalnya, disimpan ke database). Jika data tidak valid, method ini mengembalikan `False` dan akan memberikan pesan error yang sesuai.

Tanpa method `is_valid()`, kita tidak bisa memastikan bahwa data yang masuk aman dan sesuai dengan aturan yang telah dibuat. Ini penting untuk menjaga integritas data dan keamanan aplikasi.

---

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` digunakan untuk melindungi aplikasi web dari serangan CSRF (Cross-Site Request Forgery). Serangan CSRF terjadi ketika seorang penyerang mengirimkan permintaan berbahaya ke server atas nama pengguna yang telah terautentikasi. 

Jika kita tidak menambahkan `csrf_token` pada form Django, penyerang dapat membuat skrip atau link yang secara otomatis mengirimkan request ke server kita dengan memanfaatkan kredensial pengguna yang sedang aktif. Tanpa token ini, server tidak dapat memverifikasi apakah permintaan yang diterima berasal dari sumber yang sah, sehingga memungkinkan penyerang untuk melakukan tindakan yang tidak diinginkan atas nama pengguna tersebut, seperti mengubah data atau melakukan transaksi tanpa izin.

---

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### 1. Membuat Input Form untuk Menambahkan Objek Model

**Langkah-langkah**:
1. **Buat Model**: Jika belum ada, buat model yang ingin ditambahkan. Sebagai contoh, misalnya kita menggunakan model bernama `Item`:
    ```python
    # models.py
    from django.db import models

    class Item(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.name
    ```

2. **Buat Form di Django**: Buat form untuk model `Item` dengan menggunakan `ModelForm`.
    ```python
    # forms.py
    from django import forms
    from .models import Item

    class ItemForm(forms.ModelForm):
        class Meta:
            model = Item
            fields = ['name', 'description']
    ```

3. **Buat View untuk Input Form**: Buat view untuk menampilkan dan memproses form input.
    ```python
    # views.py
    from django.shortcuts import render, redirect
    from .forms import ItemForm

    def add_item(request):
        if request.method == 'POST':
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('item_list')  # Redirect ke halaman daftar item
        else:
            form = ItemForm()

        return render(request, 'add_item.html', {'form': form})
    ```

4. **Buat Template HTML**: Buat template HTML untuk menampilkan form.
    ```html
    <!-- templates/add_item.html -->
    <h2>Add New Item</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
    ```

5. **Tambahkan URL Routing untuk Form**: Tambahkan URL untuk form di `urls.py`.
    ```python
    # urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('add-item/', views.add_item, name='add_item'),
    ]
    ```

### 2. Menambahkan 4 Fungsi Views untuk Melihat Objek dalam Format XML dan JSON

**Langkah-langkah**:

1. **Buat View untuk Format JSON dan XML**: Kita akan menggunakan Django `JsonResponse` dan `HttpResponse` untuk menampilkan data dalam format JSON dan XML.

    - **View untuk JSON**:
      ```python
      # views.py
      from django.http import JsonResponse
      from .models import Item

      def item_list_json(request):
          items = list(Item.objects.values())
          return JsonResponse(items, safe=False)
      ```

    - **View untuk XML**:
      ```python
      # views.py
      from django.http import HttpResponse
      from django.core import serializers
      from .models import Item

      def item_list_xml(request):
          items = Item.objects.all()
          data = serializers.serialize('xml', items)
          return HttpResponse(data, content_type='application/xml')
      ```

    - **View untuk JSON by ID**:
      ```python
      # views.py
      from django.shortcuts import get_object_or_404

      def item_detail_json(request, id):
          item = get_object_or_404(Item, id=id)
          return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description})
      ```

    - **View untuk XML by ID**:
      ```python
      # views.py
      def item_detail_xml(request, id):
          item = get_object_or_404(Item, id=id)
          data = serializers.serialize('xml', [item])
          return HttpResponse(data, content_type='application/xml')
      ```

### 3. Membuat Routing URL untuk Masing-masing View

Tambahkan URL routing untuk masing-masing views dalam format JSON dan XML ke dalam `urls.py`.
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL untuk JSON dan XML List
    path('json/', views.item_list_json, name='item_list_json'),
    path('xml/', views.item_list_xml, name='item_list_xml'),

    # URL untuk JSON dan XML Detail by ID
    path('json/<str:id>/', views.item_detail_json, name='item_detail_json'),
    path('xml/<str:id>/', views.item_detail_xml, name='item_detail_xml'),
]
