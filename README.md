<a name="readme-top"></a>

<br />
<div align="center">
  <a href="http://samuel-taniel-tutorial.pbp.cs.ui.ac.id">
    <img src="main/templates/Pictures/pokeboy.gif" alt="To Pokemon Shop" width="80" height="80">
  </a>

<h3 align="center">Pokemon Shop</h3>

  <p align="center">
    Pengelolaan Inventory Pokemon Trading Card
    <br />
    <a href="https://github.com/SamuelTanielM/pokemon-shop"><strong>Explore the code »</strong></a>
    <br />
    <br />
    <a href="http://samuel-taniel-tutorial.pbp.cs.ui.ac.id">View Site</a>
    ·
    <a href="https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-2">View Assignment</a>
  </p>
</div>


🏪 Pokemon Shop merupakan laman yang mengelola inventory semua kartu pokemon di dunia. Lamannya masih dalam tahap pengerjaan, dan pengajuan pesanan masih belum bisa,
Tetapi Anda masih dapat menikmati kartu-kartu pokemon yang keren! ✨
<details>
  <summary>Daftar Tugas</summary>
  <ol>
    <li>
      <a href="#tugas-2">Tugas 2 | 🎴 Menginisialisasi Aplikasi Pokemon Shop</a>
    </li>
    <li>
      <a href="#tugas-3">Tugas 3 | 🃏 Membuat Form Order Pokemon Shop</a>
    </li>
    <li>
      <a href="#tugas-4">Tugas 4 | 😌 Membuat Reigster dan Login Pokemon Shop</a>
    </li>
  
<hr>
<hr>
<!-- TABLE OF CONTENTS -->
<h3 align="center">Tugas 2: Implementasi Model-View-Template (MVT) pada Django</h3>

<a name="tugas-2"></a>
<details>
<summary>Table of Contents</summary>
<ol>
  <li>
    <a href="#step-by-step">Proses Membuat Aplikasi Step-by-Step</a>
  </li>
  <li>
    <a href="#bagan-request">Bagan Request Client</a>
  </li>
  <li>
    <a href="#virtual-environment">Mengapa Menggunakan Virtual Environment</a>
    <ul>
      <li><a href="#tanpa-venv">Web Django Tanpa Virtual Environment</a></li>
    </ul>
  </li>
  <li>
    <a href="#mvc-mvt-mvvm">MVC, MVT, MVVM, dan perbedaan ketiganya</a>
    <ul>
      <li><a href="#mvc">MVC</a></li>
      <li><a href="#mvt">MVT</a></li>
      <li><a href="#mvvm">MVVM</a></li>
      <li><a href="#perbedaan">Perbedaan</a></li>
    </ul>
</ol>
</details>



<!-- ABOUT THE PROJECT -->
<a name="step-by-step"></a>
## Step by Step
<div align="center">
<a href="http://samuel-taniel-tutorial.pbp.cs.ui.ac.id">
  <img src="main/templates/Pictures/Tugas2_Web.png" alt="To Pokemon Shop" width="500" height="300">
</a>
</div>

- [X] Membuat sebuah proyek Django baru.

Hal yang dilakukan pertama oleh saya yaitu membuat direktori baru pada folder yang diinginkan disini saya membuat folder bernama "Pokemon_Shop" kemudian saya buka terminal cmdnya dan menginisialisasi environment pada direktori tersebut dengan menuju direktori tersebut dengan `cd`, kemudian menjalankan
```
python -m venv env
```
yang akan membuat file environment pada direktori itu. Kemudian untuk membuat proyek djangonya harus perlu mendownload django di environmentnya maka saya membuat folder `requirements.txt` yang berisi
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
kemudian menginstall setiap package tersebut dengan
```
pip install requirements.txt
```
Saat itu saya pernah mengalami masalah dimana package psycopg2-binary tidak dapat diinstall, yang perlu saya lakukan adalah mengupdate python saya menjadi yang terbaru dan mereboot komputer. Pastika python yang terbaru sudah ada di path dan dipindahkan ke path teratas pada environment variables. Kemudian kita dapat memulai proyek Django kita.
```
django-admin python startproject Pokemon_Shop .
```
Kemudian kita perlu membuka file `settings.py` pada folder `Pokemon_Shop` dan tambahkan `'*'` pada `ALLOWED_HOSTS` sehingga pengguna yang bisa memakai aplikasi lebih luas. Kemudian jika berhasil proyeknya akan dapat dilihat menggunakan
```
python manage.py runserver
```
yang akan berjalan pada localserver http://localhost:8000 dan menunjukkan project succesfully created.
<p></p>

karena aplikasi yang dibuat akan dideploy maka terdapat file yang perlu diignore saat dimasukkan ke github, caranya dengan saya membuat `.gitignore` yang isinya
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```

dari sini bisa membuat repositori github tetapi saya belum membuatnya dan terus lanjut membuat aplikasi pokemon_shop

- [ ] Membuat aplikasi dengan nama main pada proyek tersebut.

kemudian saya kembali kepada direktori `Pokemon_Shop` awal dan membuat direktori baru `main` fungsinya adalah merender website yang diinginkan baik dari tampilan dan dalam pemrosesan datanya. Kembali ke terminal saya jalankan line code `python manage.py startapp main` yang akan membuat aplikasi main.

- [ ] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

setelah pembuatan aplikasi main berhasil, saya menambahkan path main ke `settings.py` pada variabel `INSTALLED_APPS` pada proyek `pokemon_shop` hal ini supaya aplikasi main dapat di routing saat pengguna menggunakan `pokemon_shop`.

- [ ] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
amount sebagai jumlah item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.

Setelah aplikasi main terbuat dan dapat di routing. Saya memodifikasi file `models.py` pada direktori main, file ini berfungsi untuk mendefinisikan struktur data dan menghubungkan basis data proyeknya. Disini saya menambahkan variabel seperti yang diatas, ditambah price dan category karena aspek pembelian kartu pokemon yang berbeda-beda

- [ ] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Pada tahapan ini saya juga membuat direktori `templates` yang isinya `main.html`. Dalam file html tersebut, saya membuat tampilan website yang mau dirender, penggunaan `{{ variabel }}` mengacu pada pemetaan variabel dari `views.py` yang akan direturn ke template HTML pada tahapan selanjutnya. 

Setelah `main.html` terbentuk saya bisa memodifikasi `views.py` yang isinya fungsi yang mengembalikan data yang akan ditampilkan ke pengguna yang dipetakan ke file `main.html`. Pada `views.py` saya membuat variabel untuk nama dan kelas saya, serta tiap aspek pokemon.

#Sebenarnya pada tahapan main.html saya coba pakai css dan javascript namun sayangnya percobaan saya gagal semoga nanti di tutorial dijelaskan

- [ ] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

Untuk tahapan sebelumnya berjalan maka fungsi pada `views.py` harus dijalankan, fungsi tersebut dijalankan dengan routing dari `urls.py` yang dimasukkan path show_main nya
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
  path('', show_main, name='show_main'),
]
```
tidak lupa, saya juga menambahkan path main pada urls.py pada direktori pokemon_shop supaya dapat diakses main.urls nya dan fungsinya berjalan, seperti berikut:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('main/', include('main.urls')),
]
```

Selain itu saya membuat tests yang mengecek jika website bisa ada, bisa routing ke main, objeknya ada, dan data objek sudah benar atau belum pada `tests.py`. Dengan menambahkan fungsi seperti berikut:
```
from django.test import TestCase, Client
from main.models import Product

class mainTest(TestCase):
  def test_main_url_is_exist(self):
      response = Client().get('/main/')
      self.assertEqual(response.status_code, 200)

  def test_main_using_main_template(self):
      response = Client().get('/main/')
      self.assertTemplateUsed(response, 'main.html')

  def setUp(self):
      # membuat objek untuk di test
      Product.objects.create(name="Test Model", amount=10, price=50)  

  def test_model_exists(self): #mengecek jika objek yang dibuat ada
      model = Product.objects.get(name="Test Model", amount=10, price=50)
      self.assertIsNotNone(model)

  def test_model_properties(self): #mengecek jika data objek yang dibuat benar
      model = Product.objects.get(name="Test Model", amount=10, price=50)
      self.assertEqual(model.name, "Test Model")
      self.assertEqual(model.amount, 10)
      self.assertEqual(model.price, 50)
```
dan mengecek jika sudah benar dengan ```python manage.py test```

- [ ] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

sebelum deployment, saya pastikan semuanya sudah git add ., git commit, git push, ke github supaya saat di deploy ke adaptable dapat diakses.
Masuk ke website adaptable, pada app dashboard, create new app, kemudian pilih repositori aplikasi saya yaitu `pokemon-shop` kemudian pilih Python App template karena menggunakan python dan memilih PostgreSQL karena aplikasi yang dibuat menggunakan tipe data tersebut. Karena saya menggunakan python 3.11 saya memilih 3.11 dan memasukkan `python manage.py migrate && gunicorn shopping_list.wsgi` pada start comment yang akan memulai aplikasi pokemon_shop ketika aplikasi dibuka. Setelah itu saya menyalakan HTTP listener  on port kemudian deploy App yang kurang lebih memerlukan waktu sejaman.

- [ ] Membuat sebuah README.md

Pada file ini saya membuat readme.md nya dengan mereferensi https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md sebagai contoh readme yang baik. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<hr>

<a name="bagan-request"></a>
### Bagan Request
<div align="center">
<a href="http://samuel-taniel-tutorial.pbp.cs.ui.ac.id">
  <img src="main/templates/Pictures/Bagan_Request.jpg" alt="To Pokemon Shop" width="1000" height="500">
</a>
</div>

Pengguna menuju pada alamat aplikasi yang diinginkan dengan mengetik format URL website https:// pada box alamat website yang biasanya tersedia di atas pada browser. Tindakan tersebut berupa HTTP request yang dikirimkan dan diakses pada server World Wide Web yang tersedia dan mencari alamat yang sesuai dan di routing atau menuju alamat tersebut yang akan masuk ke routing selanjutnya pada urls.py web yang dituju. Pada `urls.py`, terdapat path routing yang mengakses aplikasi main yang isinya `views.py` berupa fungsi yang akan mereturn data, dimana basis data tersebut diatur oleh models.py. Data yang direturn `views.py` dipetakan pada file html yang berada pada folder template. File html berupa tampilan website yang akan ditampilkan kepada user yang kemudian berupa response yang akan direturn ke pengguna. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<hr>

<a name="virtual-environment"></a>
### Virtual Environment
Virtual environment merupakan space terisolasi yang dapat memiliki dependency dan packagesnya masing-masing. Hal ini memungkinkan developer untuk mengerjakan beberapa projek lainnya yang membutuhkan versi library atau package tertentu tanpa mengganggu environment lainnya atau terciptanya konflik untuk dapat berjalan dengan lancar. Cara kerjanya dengan menjalankan program `venv` atau `python -m venv <nama environment>`, kemudian `<nama environment>\Scripts\activate.bat` untuk menjalankan environmentnya pada windows. 

<a name="tanpa-venv"></a>
#### Apakah bisa membuat aplikasi tanpa virtual environment?
Pengguna bisa membuat aplikasi tanpa virtual environment, tetapi terdapat kekurangannya atau tantangannya. Contohnya jika terdapat projek yang membutuhkan Django versi tertentu, kemudian django mengalami update, maka Django pada projek tersebut juga terupdate dan dapat mengganggu jalannya program atau dependencies dan packages yang ada terutama dengan projek lain yang membutuhkan hal-hal berbeda.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<hr>

<a name="mvc-mvt-mvvm"></a>
### Penjelasan MVC, MVT, dan MVVM Serta Perbedaannya
MVC, MVT, dan MVVM adalah pola desain arsitektur yang bermanfaat untuk mengembangkan aplikasi yang mudah untuk diuji, dikelola, dan dipelihara. Pilihan pola desain yang tepat tergantung pada kebutuhan spesifik aplikasi.

<a name="mvc"></a>
#### 🏵️ MVC
MVC adalah pola desain yang paling umum digunakan. Pola ini membagi aplikasi menjadi tiga komponen utama:

Model: Komponen ini bertanggung jawab untuk menyimpan dan memanipulasi data.

View: Komponen ini bertanggung jawab untuk menampilkan semua atau beberapa data ke pengguna.

Controller: Komponen ini bertanggung jawab untuk menerima input dari pengguna dan memperbarui model dan view.

MVC popular digunakan karena mengisolasi logika aplikasi dari interface user dan memiliki penggunaan separation of concerns: pemisahan berbagai aspek atau tanggung jawab dalam aplikasi ke dalam bagian-bagian yang berbeda sehingga kode menjadi lebih terorganisir, mudah dimengerti, dan mudah difix jika ditemukan suatu masalah.

<a name="mvt"></a>
#### 🏵️ MVT
MVT (Model-View-Template), sebuah konsep arsitektur django untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Model berhubungan dengan data dan mengatur interaksi dengan data tersebut. View mengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna. template merancang tampilan yang akhirnya akan diisi dengan data dari model melalui view.

Perbedaan utama antara MVC dan MVT adalah bahwa controller dalam MVT tidak memperbarui model. Hal ini membuat model lebih mudah untuk diuji, karena model tidak perlu tahu tentang controller.

<a name="mvvm"></a>
#### 🏵️ MVVM
Model View View Model atau MVVM adalah pola desain yang lebih baru yang dikembangkan berdasarkan MVP (Model View Presenter). Dalam MVVM, view model bertanggung jawab untuk menerima input dari pengguna dan memperbarui view. View tidak berinteraksi langsung dengan model atau presenter, tetapi menerima data dari view model.


<a name="perbedaan"></a>
#### 🏵️ Perbedaan ketiga-tiganya
Perbedaan antara MVC dan MVT terdapat pada peran controller. Dalam MVC, controller menerima input dari pengguna dan memperbarui model dan view (serupa dengan MVVM). Dalam MVT, controller menerima input dari pengguna, tetapi tidak memperbarui model. Tugas memperbarui model diserahkan ke view.
Dalam MVC, controller bertanggung jawab untuk menjaga model dan view tetap sinkron. Dalam MVT, view bertanggung jawab untuk menjaga model dan view tetap sinkron.
MVC dianggap lebih fleksibel daripada MVT. Ini karena controller dalam MVC dapat menangani berbagai tugas, termasuk memperbarui model dan view. Dalam MVT, controller hanya dapat menangani tugas menerima input dari pengguna.

Sementara itu, perbedaan MVVM dan MVC terdapat pada peran view model. Dalam MVVM, view model menerima input dari pengguna dan memperbarui view. Dalam MVC, controller bertanggung jawab untuk menerima input dari pengguna dan memperbarui view. Dalam MVVM, view model bertanggung jawab untuk menjaga view tetap sinkron. Dalam MVC, controller menjaga view tetap sinkron.
Sehingga, MVVM lebih modular daripada MVC. Ini karena view model dalam MVVM dapat diuji secara terpisah dari view dan model. Dalam MVC, controller tidak dapat diuji secara terpisah dari view dan model.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<hr>
<hr>

<h3 align="center">Tugas 3: Implementasi Form dan Data Delivery pada Django</h3>

<a name="tugas-3"></a>
<details>
<summary>Table of Contents</summary>
<ol>
  <li>
    <a href="#perbedaan-post-get">Perbedaan form `POST` dan form `GET`</a>
  </li>
  <li>
    <a href="#perbedaan-pengiriman-data">Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data</a>
  </li>
  <li>
    <a href="#penggunaan-JSON">Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern</a>
  </li>
  <li>
    <a href="#step-by-step2">Step by Step Checklist Tugas</a>
  </li>
  <li>
    <a href="#screenshoot-postman">Screenshoot 5 fungsi di Postman</a>
  </li>
</ol>
</details>



<!-- ABOUT THE PROJECT -->

<a name="perbedaan-post-get"></a>
## Perbedaan form `POST` dan form `GET`

Kedua metode tersebut adalah metode dari protokol HTTP.

GET digunakan untuk meminta informasi dari sebuah API. POST digunakan untuk mengirimkan data ke sebuah API. Biasany POST digunakan untuk menambahkan record baru, PUT untuk mengirimkan versi yang diperbarui dari record, dan PATCH untuk sebagian mengirimkan record (hanya bidang-bidang yang berubah).

Dalam HTML, ada tag form yang memiliki atribut method, di mana Anda dapat menempatkan salah satu metode HTTP.

Dalam PHP, ada variabel $_POST, $_GET, dan $_REQUEST di mana Anda dapat menemukan kembali data yang dikirimkan dengan permintaan. Permintaan GET tidak mengandung data apa pun, tetapi Anda dapat mengirimkan string GET yang disebut dengan variabel yang berfungsi sebagai filter untuk permintaan Anda.

POST | GET
--- | ---
Parameter tidak dapat dilihat dalam URL, oleh karena itu, disarankan menggunakan Metode POST saat menangani informasi sensitif. | Data yang dikirimkan melalui Metode GET dapat dilihat dalam URL, oleh karena itu, Metode GET sebaiknya tidak digunakan saat menangani informasi sensitif.
Parameter tidak disimpan dalam riwayat penelusuran browser. | Karena parameter merupakan bagian dari URL, parameter tetap ada dalam riwayat penelusuran browser.
Tidak dapat ditandai sebagai favorit. | Permintaan GET dapat ditandai sebagai favorit, dan dapat disimpan dalam cache.
Permintaan POST dapat mengirimkan data hingga maksimal 8Mb. | Permintaan GET memiliki batasan panjang URL.
Contoh URL: page.php | Contoh URL: page.php?category=music
Permintaan POST cocok untuk queries di mana halaman respons berubah dari waktu ke waktu. | Permintaan GET sebaiknya digunakan untuk queries yang tidak memengaruhi apa pun di server.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="perbedaan-pengiriman-data"></a>
## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data

XML (eXtensible Markup Language) | JSON (JavaScript Object Notation) | HTML (Hypertext Markup Language)
--- | --- | ---
Mewakili data terstruktur. Ini digunakan dalam berbagai domain, termasuk layanan web, berkas konfigurasi, dan penyimpanan data. Sintaksnya sedikit lebih sulit dibandingkan JSON | Format pertukaran data ringan yang digunakan untuk mengirimkan data terstruktur antara server dan klien, atau antara bagian-bagian berbeda dari sebuah aplikasi, sintaksnya mudah dibaca | Mengatur dan menampilkan konten pada halaman web. Ini tidak dirancang untuk pertukaran data tetapi untuk membuat dokumen web dengan tautan dan pemformatan, sintaksnya susah dimengerti
file kompres sedikit lebih berat daripada JSON | file kompres JSON sedikit lebih ringan| filenya lebih berat dari ketiganya
dapat dengan mudah untuk mencari konten datanya pada nested data structure dengan XPath/Xquery | Susah untuk mengakses informasti tertentu pada nested data structure karena perlu mengetahui index/lokasi persis untuk mengambilnya| tidak memiliki antarbawaan seperti XML sehingga biasanya menggunakan JavaScript
Dapat merubah format output dengan XSLT seperti jadi HTML, text file, atau JSON | tidak memiliki built-in tool seperti XML | tidak memiliki built-in tool seperti XML tapi dapat dilakukan dengan bantuan JavaScript
lebih sulit untuk di parse daripada JSON | lebih mudah di parsed karena siap digunakan sebagai objek JavScript | HTML harus diparse menjadi model dalam DOM, lebih kompleks daripada JSON

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="penggunaan-JSON"></a>
## Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern

JSON merupakan format data yang ringan. Ini berarti data dapat dikirimkan dengan cepat melalui jaringan, mengurangi latensi dan meningkatkan kinerja aplikasi web.

terlebih dari pada itu, JSON memungkinkan kita mengatasi masalah lintas domain karena kita dapat menggunakan metode yang disebut JSONP yang menggunakan fungsi panggilan kembali (callback function) untuk mengirimkan data JSON kembali ke domain kita. Kemampuan ini yang membuat JSON sangat berguna, karena membuka banyak peluang yang sebelumnya sulit untuk diatasi.

JSON memiliki sintaks yang sederhana dan mudah dipahami oleh manusia.

Selain itu juga, mudah diproses oleh berbagai bahasa pemrograman. Sehingga, ada banyak pustaka dan dukungan bahasa pemrograman untuk mengelola JSON, yang memudahkan penggunaan dan manipulasi data JSON dalam kode Anda.

Terakhir, dapat digunakan di berbagai platform dan sistem operasi.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="step-by-step2"></a>
## Step by Step Checklist Tugas
<div align="center">
<a href="http://samuel-taniel-tutorial.pbp.cs.ui.ac.id">
  <img src="main/templates/Pictures/Tugas3_Web.png" alt="To Pokemon Shop" width="500" height="300">
</a>
</div>

- [X] Membuat input form untuk menambahkan objek model pada app sebelumnya.

Yang saya lakukan pertama adalah membuat form input datanya dengan membuat `forms.py` pada direktori `main` dengan isi seperti dibawah ini:
```
from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    # Define a list of choices for the "name" field
    NAME_CHOICES = [
        ('MewTwo', 'MewTwo'),
        ('Starmie', 'Starmie'),
        ('Eevee', 'Eevee'),
        ('Suicune', 'Suicune'),
        ('Sceptile', 'Sceptile'),
        ('Haunter', 'Haunter'),
        ('Samurott', 'Samurott'),
        ('Mimikyu', 'Mimikyu'),
        # Add more choices as needed
    ]

    # Create a ChoiceField for the "name" field with the predefined choices
    name = forms.ChoiceField(choices=NAME_CHOICES)

    class Meta:
        model = Product
        fields = ["name", "amount", "description"]
    
    def clean_amount(self):
        name = self.cleaned_data.get('name')
        amount = self.cleaned_data.get('amount')

        # Define the allowable ranges based on the selected name
        allowable_ranges = {
            'MewTwo': (0, 1),
            'Starmie': (0, 100000),
            'Eevee': (0, 100000),
            'Suicune': (0, 10000),
            'Sceptile': (0, 100000),
            'Haunter': (0, 100000),
            'Samurott': (0, 50000),
            'Mimikyu': (0, 100000),
            # Define ranges for other names here
        }

        # Check if the selected name is in the allowable_ranges dictionary
        if name in allowable_ranges:
            min_amount, max_amount = allowable_ranges[name]
            if not min_amount <= amount <= max_amount:
                raise forms.ValidationError(f"The amount for {name} must be between {min_amount} and {max_amount}!")
        
        return amount
```

Pembedahan kodenya, saya ingin memiliki dropdown form dengan nama kartu pokemon, sehingga saya memiliki `NAME_CHOICES` dan menggunakan method ChoiceField dari forms dengan `name = forms.ChoiceField(choices=NAME_CHOICES)`. Sehingga name menjadi dropdown form. Selain itu juga saya ingin membatasi jumlah amount yang dapat dibeli sesuai dengan jumlah amount yang available untuk setiap item contohnya MewTwo hanya tersedia 1 kartu sehingga pembeli maksimum membeli 1 kartu. Kekurangannya saat ada yang mengorder data pada html belum mengurang sehingga user bisa terus-menerus membeli mewtwo walaupun sudah ada yang order.. mungkin bisa dibilang order form ini bersifat waitlist :D. 

kemudian saya membuat productform sehingga input dari user berupa request yang di POST akan tersimpan. 
pertama saya import library yang ingin saya gunakan,
```
from django.http import HttpResponseRedirect
from main import forms
from django.urls import reverse
```

kemudian saya membuat isi data dari input user hal ini dilakukan pada fungsi ini:
```
def create_product(request):
    form = forms.ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
kode ini akan memvalidasi isi input dari form, dan menyimpan data dari form tersebut. 

Kemudian saya mengubah fungsi show main supaya product yang tersimpan di form bisa terbuat
```
def show_main(request):
    products = Product.objects.all()

    if products:
        last_product = products.last()
    else:
        last_product = None

    context = {
        'author_info': {
            'name': 'Samuel Taniel Mulyadi',
            'class': 'PBP D',
        },
        'app_name': 'Pokemon Shop',
        'cards': [
            {
                'picture': ...,
                'name': 'MewTwo',
                'category': 'Psychic',
                'price': 100000,
                'amount': 1,
                'description': "Mewtwo, the result of an experiment on Mew Pokemon by humans. It wants revenge on humanity, therefore there's only one of it in the world.",
            },
            ...
        'products': products,
        'last_product': last_product,
        ]
    }

    for product in products:
        total_price = 0
        picture = ""
        for card in context['cards']:
            if card['name'] == product.name:
                total_price = float(card['price']) * int(product.amount)
                picture = card['picture']
                break
            
        product.picture = picture
        product.price = total_price

    return render(request, "main.html", context)
```

hal ini mengambil seluruh object product yang tersimpan pada database sehingga dapat diakses tiap data modelnya, pada for loop tersebut setiap input dari form order akan menghitung price productnya dan menentukan gambarnya untuk dimasukkan di html. Selain itu juga ada last_product untuk memunculkan message ketika konsumer memesan order paling terakhir.

Setelah itu, saya membuat create-product.html supaya ketika ingin membuat produk/ingin mesan order akan dirouting ke html lain
```
{% extends 'base.html' %} 

{% block content %}
<h1>Order Your Card Here!</h1>
<h2>This is a waitlist order, first come first served.</h2>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Untuk mengakses routing tersebut kita dapat membuat tampilannya di main.html supaya konsumen bisa menuju ke path membuat produk kita buatkan tombol dan juga tabel yang akan menunjukkan order waitlist yang dibuat sehingga konsumen bisa tahu posisinya

```
<!-- Order Form -->
<section id="order">
  <h2>Order</h2>
  <div class="flex_center">
    <fieldset>
      <legend class="introduction">Order List</legend>    
          {% if last_product %}
          <h4>
              Thank you for your order! You have ordered {{ last_product.amount }} {{ last_product.name }} card with a total price of ${{ last_product.price }} at {{ last_product.date_added }}.
              A reminder for buyers, you are in a waitlist order. First Come First Served. Meanwhile, you can check other cards! We will contact you as soon as possible!
          </h4>
          {% endif %}
        <table>
          <tr>
              <th style="text-align: center; padding: 15px;">Display</th>
              <th style="text-align: center; padding: 15px;">Name</th>
              <th style="text-align: center; padding: 15px;">Amount</th>
              <th style="text-align: center; padding: 15px;">Price (USD)</th>
              <th style="text-align: center; padding: 15px;">Description</th>
              <th style="text-align: center; padding: 15px;">Date Added</th>
          </tr>
      
          {% comment %} memperlihatkan data produk di bawah baris ini {% endcomment %}
      
          {% for product in products %}
              <tr> 
                  <td style="text-align: center; padding: 15px;">
                    <img src={{product.picture}}
                    alt="{{product.name}}"
                    width="100"
                    height="150"/></td>
                  <td style="text-align: center; padding: 15px;"><h4>{{product.name}}</h4></td>
                  <td style="text-align: center; padding: 15px;">{{product.amount}}</td>
                  <td style="text-align: center; padding: 15px;">{{product.price}}</td>
                  <td style="text-align: center; padding: 15px;">{{product.description}}</td>
                  <td style="text-align: center; padding: 15px;">{{product.date_added}}</td>
              </tr>
          {% endfor %}
        </table>
    </fieldset>
  </div>
</section>
```

dengan begitu, konsumen dapat mengakses path ke create product dengan mudah hanya melalui klik button dan dapat melihat order lain yang telat dibuat

- [X] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

Pada file views.py terdapat 6 fungsi, untuk fungsi show html terdapat pada show_main yang akan menampilkan semua html, biasanya serialize digunakan untuk menunjukkan json, api, dan xml saja. Sesuai dengan nama fungsinya show_xml akan menunjukkan objekt produk yang telat dibuat/order dalam bentuk xml, dan seterusnya
```
def delete(request): #delete isi form
    Product.objects.all().delete()
    return HttpResponse("yoi delete")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

fungsi delete akan mendelete products yang sudah dibuat sehingga appnya akan kosong lagi

- [X] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

Saya pertama membuat routing path create-product dengan fungsi yang sudah dibuat pada views dengan mengimport fungsi tersebut pad urls.py pada direktori main supaya order form bisa dibuka
```
from main.views import show_main, create_product
```
kemudian menambahkan url patternsnya pada urls.py supaya bisa dirouting ke /create-product.

```
path('create-product', create_product, name='create_product'),
```

setelah itu menambahkan fungsi-fungsi pada views sisanya ke routing urls.py sehingga menjadi seperti ini

```
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, delete

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('delete', delete, name="delete")
]
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="screenshoot-postman"></a>
## Screenshoot 5 fungsi di Postman

➡️ Show HTML:
<div align="center">
  <img src="main/templates/Pictures/show_html.png" alt="Show HTML" width="500" height="300">
</div>

➡️ Show XML:
<div align="center">
  <img src="main/templates/Pictures/show_xml.png" alt="Show HTML" width="500" height="300">
</div>

➡️ Show JSON:
<div align="center">
  <img src="main/templates/Pictures/show_json.png" alt="Show HTML" width="500" height="300">
</div>

➡️ Show XML by ID:
<div align="center">
  <img src="main/templates/Pictures/show_xml_by_id.png" alt="Show HTML" width="500" height="300">
</div>

➡️ Show JSON by ID:
<div align="center">
  <img src="main/templates/Pictures/show_json_by_id.png" alt="Show HTML" width="500" height="300">
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="step-by-step2"></a>
## Step by Step Checklist Tugas
<div align="center">
<a href="http://samuel-taniel-tutorial.pbp.cs.ui.ac.id">
  <img src="main/templates/Pictures/Tugas3_Web.png" alt="To Pokemon Shop" width="500" height="300">
</a>
</div>

- [X] Membuat input form untuk menambahkan objek model pada app sebelumnya.

Yang saya lakukan pertama adalah membuat form input datanya dengan membuat `forms.py` pada direktori `main` dengan isi seperti dibawah ini:
```
from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    # Define a list of choices for the "name" field
    NAME_CHOICES = [
        ('MewTwo', 'MewTwo'),
        ('Starmie', 'Starmie'),
        ('Eevee', 'Eevee'),
        ('Suicune', 'Suicune'),
        ('Sceptile', 'Sceptile'),
        ('Haunter', 'Haunter'),
        ('Samurott', 'Samurott'),
        ('Mimikyu', 'Mimikyu'),
        # Add more choices as needed
    ]

    # Create a ChoiceField for the "name" field with the predefined choices
    name = forms.ChoiceField(choices=NAME_CHOICES)

    class Meta:
        model = Product
        fields = ["name", "amount", "description"]
    
    def clean_amount(self):
        name = self.cleaned_data.get('name')
        amount = self.cleaned_data.get('amount')

        # Define the allowable ranges based on the selected name
        allowable_ranges = {
            'MewTwo': (0, 1),
            'Starmie': (0, 100000),
            'Eevee': (0, 100000),
            'Suicune': (0, 10000),
            'Sceptile': (0, 100000),
            'Haunter': (0, 100000),
            'Samurott': (0, 50000),
            'Mimikyu': (0, 100000),
            # Define ranges for other names here
        }

        # Check if the selected name is in the allowable_ranges dictionary
        if name in allowable_ranges:
            min_amount, max_amount = allowable_ranges[name]
            if not min_amount <= amount <= max_amount:
                raise forms.ValidationError(f"The amount for {name} must be between {min_amount} and {max_amount}!")
        
        return amount
```

Pembedahan kodenya, saya ingin memiliki dropdown form dengan nama kartu pokemon, sehingga saya memiliki `NAME_CHOICES` dan menggunakan method ChoiceField dari forms dengan `name = forms.ChoiceField(choices=NAME_CHOICES)`. Sehingga name menjadi dropdown form. Selain itu juga saya ingin membatasi jumlah amount yang dapat dibeli sesuai dengan jumlah amount yang available untuk setiap item contohnya MewTwo hanya tersedia 1 kartu sehingga pembeli maksimum membeli 1 kartu. Kekurangannya saat ada yang mengorder data pada html belum mengurang sehingga user bisa terus-menerus membeli mewtwo walaupun sudah ada yang order.. mungkin bisa dibilang order form ini bersifat waitlist :D. 

kemudian saya membuat productform sehingga input dari user berupa request yang di POST akan tersimpan. 
pertama saya import library yang ingin saya gunakan,
```
from django.http import HttpResponseRedirect
from main import forms
from django.urls import reverse
```

kemudian saya membuat isi data dari input user hal ini dilakukan pada fungsi ini:
```
def create_product(request):
    form = forms.ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
kode ini akan memvalidasi isi input dari form, dan menyimpan data dari form tersebut. 

Kemudian saya mengubah fungsi show main supaya product yang tersimpan di form bisa terbuat
```
def show_main(request):
    products = Product.objects.all()

    if products:
        last_product = products.last()
    else:
        last_product = None

    context = {
        'author_info': {
            'name': 'Samuel Taniel Mulyadi',
            'class': 'PBP D',
        },
        'app_name': 'Pokemon Shop',
        'cards': [
            {
                'picture': ...,
                'name': 'MewTwo',
                'category': 'Psychic',
                'price': 100000,
                'amount': 1,
                'description': "Mewtwo, the result of an experiment on Mew Pokemon by humans. It wants revenge on humanity, therefore there's only one of it in the world.",
            },
            ...
        'products': products,
        'last_product': last_product,
        ]
    }

    for product in products:
        total_price = 0
        picture = ""
        for card in context['cards']:
            if card['name'] == product.name:
                total_price = float(card['price']) * int(product.amount)
                picture = card['picture']
                break
            
        product.picture = picture
        product.price = total_price

    return render(request, "main.html", context)
```

hal ini mengambil seluruh object product yang tersimpan pada database sehingga dapat diakses tiap data modelnya, pada for loop tersebut setiap input dari form order akan menghitung price productnya dan menentukan gambarnya untuk dimasukkan di html. Selain itu juga ada last_product untuk memunculkan message ketika konsumer memesan order paling terakhir.

Setelah itu, saya membuat create-product.html supaya ketika ingin membuat produk/ingin mesan order akan dirouting ke html lain
```
{% extends 'base.html' %} 

{% block content %}
<h1>Order Your Card Here!</h1>
<h2>This is a waitlist order, first come first served.</h2>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Untuk mengakses routing tersebut kita dapat membuat tampilannya di main.html supaya konsumen bisa menuju ke path membuat produk kita buatkan tombol dan juga tabel yang akan menunjukkan order waitlist yang dibuat sehingga konsumen bisa tahu posisinya

```
<!-- Order Form -->
<section id="order">
  <h2>Order</h2>
  <div class="flex_center">
    <fieldset>
      <legend class="introduction">Order List</legend>    
          {% if last_product %}
          <h4>
              Thank you for your order! You have ordered {{ last_product.amount }} {{ last_product.name }} card with a total price of ${{ last_product.price }} at {{ last_product.date_added }}.
              A reminder for buyers, you are in a waitlist order. First Come First Served. Meanwhile, you can check other cards! We will contact you as soon as possible!
          </h4>
          {% endif %}
        <table>
          <tr>
              <th style="text-align: center; padding: 15px;">Display</th>
              <th style="text-align: center; padding: 15px;">Name</th>
              <th style="text-align: center; padding: 15px;">Amount</th>
              <th style="text-align: center; padding: 15px;">Price (USD)</th>
              <th style="text-align: center; padding: 15px;">Description</th>
              <th style="text-align: center; padding: 15px;">Date Added</th>
          </tr>
      
          {% comment %} memperlihatkan data produk di bawah baris ini {% endcomment %}
      
          {% for product in products %}
              <tr> 
                  <td style="text-align: center; padding: 15px;">
                    <img src={{product.picture}}
                    alt="{{product.name}}"
                    width="100"
                    height="150"/></td>
                  <td style="text-align: center; padding: 15px;"><h4>{{product.name}}</h4></td>
                  <td style="text-align: center; padding: 15px;">{{product.amount}}</td>
                  <td style="text-align: center; padding: 15px;">{{product.price}}</td>
                  <td style="text-align: center; padding: 15px;">{{product.description}}</td>
                  <td style="text-align: center; padding: 15px;">{{product.date_added}}</td>
              </tr>
          {% endfor %}
        </table>
    </fieldset>
  </div>
</section>
```

dengan begitu, konsumen dapat mengakses path ke create product dengan mudah hanya melalui klik button dan dapat melihat order lain yang telat dibuat

- [X] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

Pada file views.py terdapat 6 fungsi, untuk fungsi show html terdapat pada show_main yang akan menampilkan semua html, biasanya serialize digunakan untuk menunjukkan json, api, dan xml saja. Sesuai dengan nama fungsinya show_xml akan menunjukkan objekt produk yang telat dibuat/order dalam bentuk xml, dan seterusnya
```
def delete(request): #delete isi form
    Product.objects.all().delete()
    return HttpResponse("yoi delete")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

fungsi delete akan mendelete products yang sudah dibuat sehingga appnya akan kosong lagi

- [X] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

Saya pertama membuat routing path create-product dengan fungsi yang sudah dibuat pada views dengan mengimport fungsi tersebut pad urls.py pada direktori main supaya order form bisa dibuka
```
from main.views import show_main, create_product
```
kemudian menambahkan url patternsnya pada urls.py supaya bisa dirouting ke /create-product.

```
path('create-product', create_product, name='create_product'),
```

setelah itu menambahkan fungsi-fungsi pada views sisanya ke routing urls.py sehingga menjadi seperti ini

```
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, delete

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('delete', delete, name="delete")
]
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="screenshoot-postman"></a>
## Screenshoot 5 fungsi di Postman

➡️ Show HTML:
<div align="center">
  <img src="main/templates/Pictures/show_html.png" alt="Show HTML" width="500" height="300">
</div>

➡️ Show XML:
<div align="center">
  <img src="main/templates/Pictures/show_xml.png" alt="Show HTML" width="500" height="300">
</div>

➡️ Show JSON:
<div align="center">
  <img src="main/templates/Pictures/show_json.png" alt="Show HTML" width="500" height="300">
</div>

➡️ Show XML by ID:
<div align="center">
  <img src="main/templates/Pictures/show_xml_by_id.png" alt="Show HTML" width="500" height="300">
</div>

➡️ Show JSON by ID:
<div align="center">
  <img src="main/templates/Pictures/show_json_by_id.png" alt="Show HTML" width="500" height="300">
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<hr>
<hr>

<h3 align="center">Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django</h3>

<a name="tugas-3"></a>
<details>
<summary>Table of Contents</summary>
<ol>
  <li>
    <a href="#usercreationform">Django UserCreationForm, Kelebihan dan Kekurangan</a>
  </li>
  <li>
    <a href="#autentikasi-dan-otorisasi">Pentingnya Autentikasi dan Otorisasi dan Perbedaannya</a>
  </li>
  <li>
    <a href="#cookies">Cookies dan Pengelolaannya oleh Django</a>
  </li>
  <li>
    <a href="#keamanan-cookies">Keamanan Penggunaan Cookies</a>
  </li>
  <li>
    <a href="#step-by-step3">Implementasi Pembuatan Web</a>
  </li>
</ol>
</details>



<!-- ABOUT THE PROJECT -->

<a name="usercreationform"></a>
## Django UserCreationForm beserta Kelebihan dan Kekurangannya

Django UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir dan memvalidasi informasi pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal. Pada aplikasi ini dibuat template html untuk register dan login, yang menggunakan fungsi dari views yang juga mengintegrasikan cookies sehingga dapat mengetahui data pengguna.

Kelebihan | Kekurangan |
--- | --- |
sudah ada built-in keamanan autentikasi usercreationform sehingga mengurangi bahaya dari cyber attack | harus mengintegrasi templatenya untuk form  |
Dimudahkan untuk dikostumasi user form yang dibutuhkan tetapi ada kekurangannya | Jika aplikasi yang dibuat membutuhkan form yang lebih spesifik atau lebih banyak maka harus membuat fungsi sendiri yang tidak disediakan |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="autentikasi-dan-otorisasi"></a>
## Pentingnya Autentikasi dan Otorisasi dan Perbedaannya

Autentikasi dan Otorisasi penting 
Pada autentikasi, user diverifikasi berdasarkan informasi yang dibuat pada web misalkan register dan login dengan isi username dan passowrd sehingga ketika user login dipastikan bahwa yang login adalah user dan bukan orang lain. Sementara itu, otorisasi adalah sebuah akses yang dapat dilakukan oleh user tergantung pada apa saja akses yang dapat dilakukan pada aplikasi, misalkan akses untuk mengubah suatu produk atau harga, dan banyak hal lainnya. 

Kedua hal ini penting karena kedua hal tersebut berkaitan dengan keamanan, sehingga terhindar dari beberapa bahaya seperti ekstorsi data, dan bahaya lainnya. Selain itu juga, mengatur siapa yang bisa mengakses API website sehingga menghindari penyalahgunaan API. Selain itu, autentikasi juga berguna supaya user dapat memiliki pengalaman yang berbeda dan lebih personal dengan data masing-masing user.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="cookies"></a>
## Cookies dan Pengelolaannya oleh Django
Cookie merupakan sebuah informasi maksimum 4kb yang dikirim oleh aplikasi web ke browser yang akan digunakan kembali atau dikirim kembali ke browser dan page request lainnya di masa depan. Cookies digunakan untuk autentikasi, user tracking, dan mengatur preferences pengguna.

Inti cara kerjanya: broswer mengirim request ke server, server mengirimm response berupa cookies ke browser, broswer menyimpan cookie tersebut sehingga setiap mengakses server, cookie yang sama akan digunakan sampai cookie kadaluarsa.

Pada django terdapat built in function untuk set_cookie pada HttpResponseRedirect, pada website ini, digunakan cookie berisi waktu terakhir login user dengan key login_user.
```
set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=None, httponly=False, samesite=None) :
```
Kemudian website dapat merequest cookie yang diberikan di awal untuk keperluan di masa depan dengan ```request.COOKIES```, pada aplikasi ini di views.py yang dirouting dari urls.py pada main juga untuk ditampilkan isi last_login pada template main.html

Kemudian terdapat ```delete_cookie``` dengan menerima key untuk menghapus cookie.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="keamanan-cookies"></a>
## Keamanan Penggunaan Cookies
Karena cookies hanyalah informasi kecil yang digunakan oleh website tentang user, cookies secara default aman karena tidak dapat membaca atau menghapus data user, dan biasanya anonim atau tidak mengandung data pribadi pengguna. Terkait jenisnya ada perbedaan pada keamanannya, pada session cookie (default): temporary cookie, cookie tersebut hanya browser yang dapat mengakses dan di delete ketika broswer ditutup sehingga informasi yang digunakan hanyalah sementara. Sementara itu, persistent cookie tersimpan pada komputer pengakses dimana user atau program dapat membuka cookie tersebut sehingga kurang aman.

Sehingga terdapat risiko potensial yang harus diwaspadai yaitu:
cookie yang digunakan dapat digunakan untuk mentrack akitivtas online seperti user preferences yang dapat digunakan beberapa website seperti e-commerce dan ad/iklan. Sehingga ketika, cookie tersebut diambil oleh seseorang dengan maksud yang jahat mereka dapat menggunakan cookie tersebut untuk kepentingan mereka. Contohnya jika website menjual informasi yang didapat dari cookie ke pihak ketiga.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="step-by-step3"></a>
## Step by Step Checklist Tugas
<div align="center">
<a href="http://samuel-taniel-tutorial.pbp.cs.ui.ac.id">
  <img src="main/templates/Pictures/Tugas4_Web.png" alt="To Pokemon Shop" width="500" height="300">
</a>
</div>

- [X] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

Pada website pokemon shop digunakan UserCreationForm impor dari django library

> pada fungsi register UserCreationForm berdasarkan request.POST oleh user berupa input ke dalam QueryDict yang akan disimpan datanya dengan .save() dan sebelumnya di cek dengan is_valid selama formnya valid dan akan menampilkan message kalau akunnya berhasil dibuat

```

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created! You are now able to order cards or just look around!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

> Pada fungsi login mengimport authenticate dan login, authenticate unutk mengautentikasi pengguna dengan username dan password dari pengguna (request) saat login, dan login digunakan untuk mengambil data user yang sudah diregister dan akan ditampilkan/digunakan untuk data yang personal tiap user yang berbeda

pada fungsi ini juga diset cookienya sesuai dengan jam loginnya untuk mengecek terakhir kali login
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry Pokemon Trainer, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

> Terakhir terdapat fungsi untuk logout yang menggunakan import logout dari django yang dilengkapi dengan cookie delete sehingga termasuk session cookie/temp cookie

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

kemudian ketigas fungsi tersebut digunakan untuk register.html untuk fungsi register, login.html untuk fungsi login pada main/templates dan logout pada main.html dan ketiganya di route di urls.py pada main.

- [X] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Untuk membuat tiga dummy data yang menggunakan model untuk dua akun saya memanfaatkan model baru dimana tiap produk memiliki atribut user. 

```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    picture = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    price = models.IntegerField(blank=True, null=True)
    allow_range = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255)
    description = models.TextField()
```

Sehingga kita website dijalankan, user yang login hanya akan ditampilkan produk miliknya berikut contoh dua user dengan tiga dummy data berbeda:
pertama kita buat dahulu 2 akun, contoh 2 akun yaitu pertama kita akses websitenya kemudian akan berada pada halaman login, buat dua akun dengan klik register now yang akan di route ke register dimana kita bisa memasukkan datanya
```
Akun pertama
Username: samuel.taniel
Password: saljunyacoklat

kemudian balik ke login register now lagi

Akun kedua
Username: santen.kelapa
Password: saljunyacoklat
```

kemudian kita login pada akun pertama dengan kredensial tersebut, dan klik add new product masukkan product yang diinginkan sebanyak 3 kali kemudian logout lalu login pada akun kedua lakukan hal yang sama dengan produk berbeda. Maka jika kita kembali login pada akun pertama, tampilan produk yang dipesan akan berbeda dengan akun kedua.

- [X]  Menghubungkan model Item dengan User.
Disini saya menggabungkan username user dengan produk sehingga ketika ditampilkan akan menunjukkan item tiap user berbeda sesuai yang di pesan pada fungsi create_product di views.py
```
def create_product(request):
    form = forms.ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)
```

- [X] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

Dengan memasukkan data user dengan request pada views.py
```
'login_info': {
    'name': request.user.username,
    'user': request.user,
},
```

kita dapat mengakses di main.html 

```
<div class="profile_name">
  <a>Author Info</a>
  <a style="float: right; padding-right: 1cm;">Login Info</a>
</div>
<div class="login_info">
  <img src="https://cdn-icons-png.flaticon.com/512/1828/1828439.png" width="20" height="20"/>
  <a>{{ author_info.name }}</a>
  <a style="float: right; padding-right: 1cm;">{{ login_info.name }}</a>
  <div class="contact_info">
    <img src="https://cdn-icons-png.flaticon.com/512/185/185578.png" width="20" height="20"/>
  {{ author_info.class }}
</div>
```

- [X] Tambahkan tombol dan fungsi untuk menambahkan amount suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.

Pada checklist bonus ini saya menmanfaatkan atribut pk untuk tiap item sehingga cara kerjanya adalah dengan mencocokan id pk dari request user pada button untuk memanggil fungsi increase_item_amount maka objeknya akan bertambah, sama halnya pada fungsi decrease_item_amount yang akan mengurangi item amount. Pada penjumlahan item yang diorder hanya bsia sesuai dengan maksimal item yang ada, dan decrease_item_amount ketika kurang dari sama dengan 0 akan menghapus itemnya. 

```
def decrease_item_amount(request, id):
    products = Product.objects.all()
    for product in products:
        if product.pk == id:
            break
    
    product.amount -= 1
    if (product.amount <= 0):
        product.delete()
    product.save()
    
    return redirect('main:show_main')

def increase_item_amount(request, id):
    products = Product.objects.all()
    for product in products:
        if product.pk == id:
            break
    
    product.amount += 1
    if(product.allow_range):
        if (product.amount > product.allow_range):
            product.amount -= 1
    product.save()
    
    return redirect('main:show_main')
```

- [X] Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori.

Sama cara pikirnya pada sebelumnya perbedaannya product akan dihapus dengan method delete bawaan Django models

```
def delete_item(request, id):
    products = Product.objects.all()
    for product in products:
        if product.pk == id:
            break

    product.delete()
    
    return redirect('main:show_main')
```


  </ol>
</details>
