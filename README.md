Nama  : Naomi Kyla Zahra Siregar
NPM   : 2406434102
Kelas : PBP - B

TUGAS 2 "IMPLEMENTASI MODEL-VIEW-TEMPLATE (MVT) PADA DJANGO"

Nama Project: goollmart
Link Deployment PWS: https://pbp.cs.ui.ac.id/naomi.kyla/goollmart

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img width="1024" height="768" alt="Bagan Alur Request-Response Django-2" src="https://github.com/user-attachments/assets/99f80b87-802d-4dbd-a03a-a14dcfac88a2" />

3. Jelaskan peran settings.py dalam proyek Django!
File settings.py berfungsi sebagai pusat konfigurasi utama pada proyek Django. Beberapa hal penting yang diatur di sini antara lain:
- daftar aplikasi yang digunakan (INSTALLED_APPS),
- konfigurasi database,
- middleware,
- pengaturan file statis,
- mode debug serta daftar host yang diizinkan.
Tanpa file settings.py, proyek Django tidak akan memiliki konfigurasi dasar untuk berjalan dengan baik.

4. Bagaimana cara kerja migrasi database di Django?
Migrasi di Django terdiri dari dua tahap:
1) makemigrations → Django membuat file migrasi berisi instruksi SQL berdasarkan perubahan pada model.
2) migrate → Django mengeksekusi file migrasi tersebut ke database sehingga struktur tabel sesuai dengan model Python yang telah dibuat.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya Django cocok dipakai sebagai framework pembelajaran karena:
- Django merupakan framework web open source yang bebas digunakan.
- Django mendukung pengembangan dengan cepat, sehingga memudahkan dalam membangun aplikasi web.
- Django sudah dilengkapi banyak fitur bawaan sehingga tidak perlu selalu menambahkan library eksternal.
- Django memiliki standar keamanan yang baik, sehingga cukup aman digunakan.
- Django bersifat scalable, dapat dipakai untuk aplikasi kecil maupun besar.
- Django sangat versatile, bisa digunakan untuk membangun berbagai jenis aplikasi dengan beragam kebutuhan.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Menurut saya, penjelasan asisten dosen pada tutorial 1 sangat jelas, terutama melalui tulisan tutorial yang disediakan. Walaupun kegiatan tutorial 1 saat itu dilaksanakan secara online dari rumah masing-masing, saya tetap bisa mengikuti dan memahami step-by-step yang diberikan dengan baik. Penjelasannya runtut, detail, dan mudah dipahami, sehingga tidak membingungkan.
