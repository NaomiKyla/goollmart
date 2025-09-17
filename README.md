Nama  : Naomi Kyla Zahra Siregar
NPM   : 2406434102
Kelas : PBP - B

#**TUGAS 2 "IMPLEMENTASI MODEL-VIEW-TEMPLATE (MVT) PADA DJANGO"**#

Nama Project: goollmart
Link Deployment PWS: https://naomi-kyla-goollmart.pbp.cs.ui.ac.id

**1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Berikut implementasi checklist secara step-by-step.
1) Membuat proyek Django baru
Pertama saya membuat folder proyek bernama goollmart dan mengaktifkan virtual environment. Setelah itu saya install Django lalu membuat proyek baru dengan nama yang sama.
2) Membuat aplikasi main 
Setelah proyek berhasil dibuat, saya menambahkan aplikasi baru bernama main yang menjadi inti logika program.
3) Mendaftarkan aplikasi ke settings
Di file goollmart/settings.py, saya menambahkan main pada bagian INSTALLED_APPS agar Django mengenali aplikasi tersebut.
4) Membuat model Product
Pada file main/models.py, saya membuat model Product dengan atribut: name, price, description, thumbnail, category, dan is_featured.
5) Migrasi database
Saya menjalankan makemigrations dan migrate untuk membuat file migrasi sekaligus menyesuaikan database dengan model yang sudah didefinisikan.
6) Membuat view
Di main/views.py saya menambahkan fungsi show_main yang mengirimkan context berupa identitas (npm, nama, kelas) untuk dirender ke template.
7) Routing URL
Saya membuat file urls.py di dalam aplikasi main dan menghubungkannya dengan goollmart/urls.py, sehingga request ke root diarahkan ke fungsi show_main.
8) Membuat template
Saya membuat file main.html di folder main/templates/ yang digunakan untuk menampilkan informasi identitas dan nama aplikasi.
9) Menjalankan server lokal
Setelah semuanya siap, saya jalankan perintah python manage.py runserver untuk memastikan aplikasi bisa berjalan di browser.
10) Membuat unit test sederhana
Saya menuliskan beberapa test di tests.py untuk memastikan URL utama bisa diakses, template yang digunakan sesuai, dan data identitas tampil di halaman.
11) Push ke GitHub & deploy ke PWS
Setelah semua selesai, saya upload proyek ke repository GitHub lalu push juga ke PWS agar aplikasi bisa diakses online.

**2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
<img width="1024" height="768" alt="Bagan Alur Request-Response Django-2" src="https://github.com/user-attachments/assets/99f80b87-802d-4dbd-a03a-a14dcfac88a2" />

**3. Jelaskan peran settings.py dalam proyek Django!**
File settings.py berfungsi sebagai pusat konfigurasi utama pada proyek Django. Beberapa hal penting yang diatur di sini antara lain:
- daftar aplikasi yang digunakan (INSTALLED_APPS),
- konfigurasi database,
- middleware,
- pengaturan file statis,
- mode debug serta daftar host yang diizinkan.
Tanpa file settings.py, proyek Django tidak akan memiliki konfigurasi dasar untuk berjalan dengan baik.

**4. Bagaimana cara kerja migrasi database di Django?**
Migrasi di Django terdiri dari dua tahap:
1) makemigrations → Django membuat file migrasi berisi instruksi SQL berdasarkan perubahan pada model.
2) migrate → Django mengeksekusi file migrasi tersebut ke database sehingga struktur tabel sesuai dengan model Python yang telah dibuat.

**5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Menurut saya Django cocok dipakai sebagai framework pembelajaran karena:
- Django merupakan framework web open source yang bebas digunakan.
- Django mendukung pengembangan dengan cepat, sehingga memudahkan dalam membangun aplikasi web.
- Django sudah dilengkapi banyak fitur bawaan sehingga tidak perlu selalu menambahkan library eksternal.
- Django memiliki standar keamanan yang baik, sehingga cukup aman digunakan.
- Django bersifat scalable, dapat dipakai untuk aplikasi kecil maupun besar.
- Django sangat versatile, bisa digunakan untuk membangun berbagai jenis aplikasi dengan beragam kebutuhan.

**6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**
Menurut saya, penjelasan asisten dosen pada tutorial 1 sangat jelas, terutama melalui tulisan tutorial yang disediakan. Walaupun kegiatan tutorial 1 saat itu dilaksanakan secara online dari rumah masing-masing, saya tetap bisa mengikuti dan memahami step-by-step yang diberikan dengan baik. Penjelasannya runtut, detail, dan mudah dipahami, sehingga tidak membingungkan.
<<<<<<< HEAD

#**TUGAS 3 "Implementasi Form dan Data Delivery pada Django"**#

**1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery penting karena web bekerja dengan komunikasi antara client (browser) dan server melalui HTTP request–response. Platform butuh cara untuk mengirim dan menerima data agar bisa menampilkan informasi dinamis, bukan sekadar HTML statis.

**2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
Menurut saya, JSON lebih unggul dibandingkan XML karena memiliki struktur yang ringkas dan mudah dipahami. Berbeda dengan JSON, XML menggunakan banyak tag pembuka dan penutup yang membuat dokumennya lebih panjang dan kompleks sehingga kurang praktis dibaca. Selain itu, JSON terintegrasi langsung dengan JavaScript sehingga bisa digunakan tanpa proses konversi tambahan. Dukungan bawaan pada berbagai bahasa pemrograman juga membuat JSON lebih sederhana untuk diproses dan diserialisasi.

**3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
is_valid() digunakan untuk melakukan validasi input di form Django. Method ini akan:
•	Mengecek apakah data yang di-submit sesuai dengan tipe field di model.
•	Mengembalikan True jika data valid, False jika ada error.
is_valid() dibutuhkan supaya data yang masuk ke database lewat ProductForm bersih dan konsisten. Kalau tanpa validasi, input bisa berantakan (misalnya harga diisi huruf).

**4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
csrf_token adalah token keamanan untuk mencegah CSRF (Cross-Site Request Forgery).
Jika csrf_token  tidak ditambahkan:
•	Penyerang bisa membuat user tanpa sadar mengirim request ke aplikasi kita (misalnya lewat form palsu).
•	Akibatnya data di server bisa dimodifikasi tanpa izin.
Dengan token unik di tiap request, hanya form sah dari server yang bisa diterima oleh Django.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Langkah yang saya lakukan:
**1.	Membuat forms.py di folder main**
Tujuannya adalah membuat form khusus untuk model Product, sehingga kita bisa menangani input data dari user dengan lebih terstruktur dan aman.
**2.	Membuat views.py di folder main**
Di sini dibuat fungsi create_product yang bertanggung jawab untuk menerima data dari form dan menyimpan produk baru ke database.
**3.	Membuat create_product.html di folder templates/main**
File ini berisi form HTML yang memungkinkan user memasukkan data produk baru melalui antarmuka web.
**4.	Menambahkan csrf_token pada form di create_product.html**
Tujuannya adalah untuk melindungi form dari serangan CSRF (Cross-Site Request Forgery), sehingga hanya request yang sah yang bisa diterima.
**5.	Menambahkan fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id di views.py**
Fungsi-fungsi ini dibuat untuk menampilkan data Product dalam format XML atau JSON, baik seluruh data maupun data berdasarkan ID tertentu.
**6.	Membuat urls.py di folder main**
File ini digunakan untuk mendefinisikan routing, sehingga setiap URL yang dikunjungi akan diarahkan ke fungsi view yang sesuai.

**6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**
Menurut saya, tutorial 2 dari asdos sangat membantu dan penjelasannya jelas sehingga memudahkan dalam memahami langkah-langkah praktikum. Selain itu, asdos juga mengadakan Discord voice channel untuk menjelaskan lebih lanjut terkait tutorial, yang menurut saya sangat berguna.

**Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**

<img width="1470" height="956" alt="Screenshot 2025-09-16 at 22 26 40" src="https://github.com/user-attachments/assets/20a60466-c42d-46ed-a22a-cfd283b62354" />

<img width="1470" height="956" alt="Screenshot 2025-09-16 at 22 27 20" src="https://github.com/user-attachments/assets/973ab7b0-1f7a-49b8-9df0-77405887f583" />

<img width="1470" height="956" alt="Screenshot 2025-09-16 at 22 34 12" src="https://github.com/user-attachments/assets/5befa09e-dada-4a49-a9b1-41119603a1bf" />

<img width="1470" height="956" alt="Screenshot 2025-09-16 at 22 34 46" src="https://github.com/user-attachments/assets/9c095392-c4d3-4384-8cc1-9bd350847f4b" />
















