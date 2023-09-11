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
      <ul>
        <li><a href="#penjelasan">Penjelasan</a></li>
      </ul>
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

kemudian saya kembali kepada direktori `Pokemon_Shop` awal dan membuat direktori baru `main` fungsinya adalah merender website yang diinginkan baik dari tampilan dan dalam pemrosesan datanya

- [ ] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- [ ] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
amount sebagai jumlah item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.

- [ ] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [ ] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- [ ] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [ ] Membuat sebuah README.md

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<a name="bagan-request"></a>
### Bagan Request


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="penjelasan"></a>
### Bagan Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="virtual-environment"></a>
### Bagan Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="tanpa-venv"></a>
### Bagan Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="mvc-mvt-mvvm"></a>
### Bagan Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="mvc"></a>
### Bagan Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="mvt"></a>
### Bagan Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="mvvm"></a>
### Bagan Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<a name="perbedaan"></a>
### Bagan Request
<p align="right">(<a href="#readme-top">back to top</a>)</p>
