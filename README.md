<a name="readme-top"></a>

<br />
<div align="center">
  <a href="https://pokemon-shop.adaptable.app/main/">
    <img src="https://64.media.tumblr.com/088786d466c3a315d6043b8e59d96770/tumblr_msu2ojWkqz1scncwdo1_500.gif" alt="To Pokemon Shop" width="80" height="80">
  </a>

<h3 align="center">Pokemon Shop</h3>

  <p align="center">
    Pengelolaan Inventory Pokemon Trading Card
    <br />
    <a href="https://github.com/SamuelTanielM/pokemon-shop"><strong>Explore the code »</strong></a>
    <br />
    <br />
    <a href="https://pokemon-shop.adaptable.app/main/">View Site</a>
    ·
    <a href="https://pbp-fasilkom-ui.github.io/ganjil-2024/assignments/individual/assignment-2">View Assignment</a>
  </p>
</div>


Pokemon Shop merupakan laman yang mengelola inventory semua kartu pokemon di dunia. Lamannya masih dalam tahap pengerjaan, dan pengajuan pesanan masih belum bisa,
Tetapi Anda masih dapat menikmati kartu-kartu pokemon yang keren!

<!-- TABLE OF CONTENTS -->
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
<a href="https://pokemon-shop.adaptable.app/main/">
    <img src="https://github.com/SamuelTanielM/pokemon-shop/blob/main/main/templates/images_html/Screenshot%202023-09-11%20151852.png" alt="To Pokemon Shop" width="500" height="300">
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

- [ ] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

sebelum deployment, saya pastikan semuanya sudah git add ., git commit, git push, ke github supaya saat di deploy ke adaptable dapat diakses.
Masuk ke website adaptable, pada app dashboard, create new app, kemudian pilih repositori aplikasi saya yaitu `pokemon-shop` kemudian pilih Python App template karena menggunakan python dan memilih PostgreSQL karena aplikasi yang dibuat menggunakan tipe data tersebut. Karena saya menggunakan python 3.11 saya memilih 3.11 dan memasukkan `python manage.py migrate && gunicorn shopping_list.wsgi` pada start comment yang akan memulai aplikasi pokemon_shop ketika aplikasi dibuka. Setelah itu saya menyalakan HTTP listener  on port kemudian deploy App yang kurang lebih memerlukan waktu sejaman.

- [ ] Membuat sebuah README.md

Pada file ini saya membuat readme.md nya dengan mereferensi https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md sebagai contoh readme yang baik. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="bagan-request"></a>
### Bagan Request
<div align="center">
<a href="https://pokemon-shop.adaptable.app/main/">
    <img src="https://github.com/SamuelTanielM/pokemon-shop/blob/main/main/templates/images_html/Bagan%20Request.jpg" alt="To Pokemon Shop" width="950" height="500">
  </a>
</div>

Pengguna menuju pada alamat aplikasi yang diinginkan dengan mengetik format URL website https:// pada box alamat website yang biasanya tersedia di atas pada browser. Tindakan tersebut berupa HTTP request yang dikirimkan dan diakses pada server World Wide Web yang tersedia dan mencari alamat yang sesuai dan di routing atau menuju alamat tersebut yang akan masuk ke routing selanjutnya pada urls.py web yang dituju. Pada `urls.py`, terdapat path routing yang mengakses aplikasi main yang isinya `views.py` berupa fungsi yang akan mereturn data, dimana basis data tersebut diatur oleh models.py. Data yang direturn `views.py` dipetakan pada file html yang berada pada folder template. File html berupa tampilan website yang akan ditampilkan kepada user yang kemudian berupa response yang akan direturn ke pengguna. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="virtual-environment"></a>
### Virtual Environment
<p align="right">(<a href="#readme-top">back to top</a>)</p>

Virtual environment merupakan space terisolasi yang dapat memiliki dependency dan packagesnya masing-masing. Hal ini memungkinkan developer untuk mengerjakan beberapa projek lainnya yang membutuhkan versi library atau package tertentu tanpa mengganggu environment lainnya atau terciptanya konflik untuk dapat berjalan dengan lancar. Cara kerjanya dengan menjalankan program `venv` atau `python -m venv <nama environment>`, kemudian `<nama environment>\Scripts\activate.bat` untuk menjalankan environmentnya pada windows. 

<a name="tanpa-venv"></a>
#### Apakah bisa membuat aplikasi tanpa virtual environment?
Pengguna bisa membuat aplikasi tanpa virtual environment, tetapi terdapat kekurangannya atau tantangannya. Contohnya jika terdapat projek yang membutuhkan Django versi tertentu, kemudian django mengalami update, maka Django pada projek tersebut juga terupdate dan dapat mengganggu jalannya program atau dependencies dan packages yang ada terutama dengan projek lain yang membutuhkan hal-hal berbeda.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="mvc-mvt-mvvm"></a>
### Penjelasan MVC, MVT, dan MVVM Serta Perbedaannya
MVC, MVT, dan MVVM adalah pola desain arsitektur yang bermanfaat untuk mengembangkan aplikasi yang mudah untuk diuji, dikelola, dan dipelihara. Pilihan pola desain yang tepat tergantung pada kebutuhan spesifik aplikasi.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="mvc"></a>
#### MVC
MVC adalah pola desain yang paling umum digunakan. Pola ini membagi aplikasi menjadi tiga komponen utama:

Model: Komponen ini bertanggung jawab untuk menyimpan dan memanipulasi data.

View: Komponen ini bertanggung jawab untuk menampilkan semua atau beberapa data ke pengguna.

Controller: Komponen ini bertanggung jawab untuk menerima input dari pengguna dan memperbarui model dan view.

MVC popular digunakan karena mengisolasi logika aplikasi dari interface user dan memiliki penggunaan separation of concerns: pemisahan berbagai aspek atau tanggung jawab dalam aplikasi ke dalam bagian-bagian yang berbeda sehingga kode menjadi lebih terorganisir, mudah dimengerti, dan mudah difix jika ditemukan suatu masalah.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="mvt"></a>
#### MVT
MVT (Model-View-Template), sebuah konsep arsitektur django untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Model berhubungan dengan data dan mengatur interaksi dengan data tersebut. View mengatur tampilan dan mengambil data dari model untuk disajikan kepada pengguna. template merancang tampilan yang akhirnya akan diisi dengan data dari model melalui view.

Perbedaan utama antara MVC dan MVT adalah bahwa controller dalam MVT tidak memperbarui model. Hal ini membuat model lebih mudah untuk diuji, karena model tidak perlu tahu tentang controller.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="mvvm"></a>
#### MVVM
Model View View Model atau MVVM adalah pola desain yang lebih baru yang dikembangkan berdasarkan MVP (Model View Presenter). Dalam MVVM, view model bertanggung jawab untuk menerima input dari pengguna dan memperbarui view. View tidak berinteraksi langsung dengan model atau presenter, tetapi menerima data dari view model.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="perbedaan"></a>
#### Perbedaan ketiga-tiganya
Perbedaan antara MVC dan MVT terdapat pada peran controller. Dalam MVC, controller menerima input dari pengguna dan memperbarui model dan view (serupa dengan MVVM). Dalam MVT, controller menerima input dari pengguna, tetapi tidak memperbarui model. Tugas memperbarui model diserahkan ke view.
Dalam MVC, controller bertanggung jawab untuk menjaga model dan view tetap sinkron. Dalam MVT, view bertanggung jawab untuk menjaga model dan view tetap sinkron.
MVC dianggap lebih fleksibel daripada MVT. Ini karena controller dalam MVC dapat menangani berbagai tugas, termasuk memperbarui model dan view. Dalam MVT, controller hanya dapat menangani tugas menerima input dari pengguna.

Sementara itu, perbedaan MVVM dan MVC terdapat pada peran view model. Dalam MVVM, view model menerima input dari pengguna dan memperbarui view. Dalam MVC, controller bertanggung jawab untuk menerima input dari pengguna dan memperbarui view. Dalam MVVM, view model bertanggung jawab untuk menjaga view tetap sinkron. Dalam MVC, controller menjaga view tetap sinkron.
Sehingga, MVVM lebih modular daripada MVC. Ini karena view model dalam MVVM dapat diuji secara terpisah dari view dan model. Dalam MVC, controller tidak dapat diuji secara terpisah dari view dan model.
<p align="right">(<a href="#readme-top">back to top</a>)</p>
