# Naomi Kyla Zahra Siregar
**NPM:** 2406434102  
**Kelas:** PBP - B  

---

## TUGAS 2: IMPLEMENTASI MODEL-VIEW-TEMPLATE (MVT) PADA DJANGO

**Nama Project:** goollmart  
**Link Deployment PWS:** [https://naomi-kyla-goollmart.pbp.cs.ui.ac.id](https://naomi-kyla-goollmart.pbp.cs.ui.ac.id)  

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
Berikut implementasi checklist secara step-by-step:  

1) **Membuat proyek Django baru**  
Pertama saya membuat folder proyek bernama goollmart dan mengaktifkan virtual environment. Setelah itu saya install Django lalu membuat proyek baru dengan nama yang sama.  

2) **Membuat aplikasi main**  
Setelah proyek berhasil dibuat, saya menambahkan aplikasi baru bernama main yang menjadi inti logika program.  

3) **Mendaftarkan aplikasi ke settings**  
Di file goollmart/settings.py, saya menambahkan main pada bagian INSTALLED_APPS agar Django mengenali aplikasi tersebut.  

4) **Membuat model Product**  
Pada file main/models.py, saya membuat model Product dengan atribut: name, price, description, thumbnail, category, dan is_featured.  

5) **Migrasi database**  
Saya menjalankan makemigrations dan migrate untuk membuat file migrasi sekaligus menyesuaikan database dengan model yang sudah didefinisikan.  

6) **Membuat view**  
Di main/views.py saya menambahkan fungsi show_main yang mengirimkan context berupa identitas (npm, nama, kelas) untuk dirender ke template.  

7) **Routing URL**  
Saya membuat file urls.py di dalam aplikasi main dan menghubungkannya dengan goollmart/urls.py, sehingga request ke root diarahkan ke fungsi show_main.  

8) **Membuat template**  
Saya membuat file main.html di folder main/templates/ yang digunakan untuk menampilkan informasi identitas dan nama aplikasi.  

9) **Menjalankan server lokal**  
Setelah semuanya siap, saya jalankan perintah python manage.py runserver untuk memastikan aplikasi bisa berjalan di browser.  

10) **Membuat unit test sederhana**  
Saya menuliskan beberapa test di tests.py untuk memastikan URL utama bisa diakses, template yang digunakan sesuai, dan data identitas tampil di halaman.  

11) **Push ke GitHub & deploy ke PWS**  
Setelah semua selesai, saya upload proyek ke repository GitHub lalu push juga ke PWS agar aplikasi bisa diakses online.  

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
<img width="1024" height="768" alt="Bagan Alur Request-Response Django-2" src="https://github.com/user-attachments/assets/99f80b87-802d-4dbd-a03a-a14dcfac88a2" />

### 3. Jelaskan peran settings.py dalam proyek Django
File settings.py berfungsi sebagai pusat konfigurasi utama pada proyek Django. Beberapa hal penting yang diatur di sini antara lain:  
- daftar aplikasi yang digunakan (INSTALLED_APPS)  
- konfigurasi database  
- middleware  
- pengaturan file statis  
- mode debug serta daftar host yang diizinkan  

Tanpa file settings.py, proyek Django tidak akan memiliki konfigurasi dasar untuk berjalan dengan baik.  

### 4. Bagaimana cara kerja migrasi database di Django
Migrasi di Django terdiri dari dua tahap:  
1) **makemigrations** → Django membuat file migrasi berisi instruksi SQL berdasarkan perubahan pada model.  
2) **migrate** → Django mengeksekusi file migrasi tersebut ke database sehingga struktur tabel sesuai dengan model Python yang telah dibuat.  

### 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Menurut saya Django cocok dipakai sebagai framework pembelajaran karena:  
- Django merupakan framework web open source yang bebas digunakan.  
- Django mendukung pengembangan dengan cepat, sehingga memudahkan dalam membangun aplikasi web.  
- Django sudah dilengkapi banyak fitur bawaan sehingga tidak perlu selalu menambahkan library eksternal.  
- Django memiliki standar keamanan yang baik, sehingga cukup aman digunakan.  
- Django bersifat scalable, dapat dipakai untuk aplikasi kecil maupun besar.  
- Django sangat versatile, bisa digunakan untuk membangun berbagai jenis aplikasi dengan beragam kebutuhan.  

### 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya
Menurut saya, penjelasan asisten dosen pada tutorial 1 sangat jelas, terutama melalui tulisan tutorial yang disediakan. Walaupun kegiatan tutorial 1 saat itu dilaksanakan secara online dari rumah masing-masing, saya tetap bisa mengikuti dan memahami step-by-step yang diberikan dengan baik. Penjelasannya runtut, detail, dan mudah dipahami, sehingga tidak membingungkan.  

---

## TUGAS 3: IMPLEMENTASI FORM DAN DATA DELIVERY PADA DJANGO

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Data delivery penting karena web bekerja dengan komunikasi antara client (browser) dan server melalui HTTP request–response. Platform butuh cara untuk mengirim dan menerima data agar bisa menampilkan informasi dinamis, bukan sekadar HTML statis.  

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML
Menurut saya, JSON lebih unggul dibandingkan XML karena memiliki struktur yang ringkas dan mudah dipahami. Berbeda dengan JSON, XML menggunakan banyak tag pembuka dan penutup yang membuat dokumennya lebih panjang dan kompleks sehingga kurang praktis dibaca. Selain itu, JSON terintegrasi langsung dengan JavaScript sehingga bisa digunakan tanpa proses konversi tambahan. Dukungan bawaan pada berbagai bahasa pemrograman juga membuat JSON lebih sederhana untuk diproses dan diserialisasi.  

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut
is_valid() digunakan untuk melakukan validasi input di form Django. Method ini akan:  
- Mengecek apakah data yang di-submit sesuai dengan tipe field di model.  
- Mengembalikan True jika data valid, False jika ada error.  

is_valid() dibutuhkan supaya data yang masuk ke database lewat ProductForm bersih dan konsisten. Kalau tanpa validasi, input bisa berantakan (misalnya harga diisi huruf).  

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang
csrf_token adalah token keamanan untuk mencegah CSRF (Cross-Site Request Forgery).  
Jika csrf_token tidak ditambahkan:  
- Penyerang bisa membuat user tanpa sadar mengirim request ke aplikasi kita (misalnya lewat form palsu).  
- Akibatnya data di server bisa dimodifikasi tanpa izin.  

Dengan token unik di tiap request, hanya form sah dari server yang bisa diterima oleh Django.  

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
1) **Membuat forms.py di folder main**  
   Tujuannya adalah membuat form khusus untuk model Product, sehingga kita bisa menangani input data dari user dengan lebih terstruktur dan aman.  

2) **Membuat views.py di folder main**  
   Fungsi create_product yang bertanggung jawab untuk menerima data dari form dan menyimpan produk baru ke database.  

3) **Membuat create_product.html di folder templates/main**  
   File ini berisi form HTML yang memungkinkan user memasukkan data produk baru melalui antarmuka web.  

4) **Menambahkan csrf_token pada form di create_product.html**  
   Tujuannya adalah untuk melindungi form dari serangan CSRF.  

5) **Menambahkan fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id di views.py**  
   Fungsi-fungsi ini dibuat untuk menampilkan data Product dalam format XML atau JSON, baik seluruh data maupun data berdasarkan ID tertentu.  

6) **Membuat urls.py di folder main**  
   File ini digunakan untuk mendefinisikan routing, sehingga setiap URL yang dikunjungi akan diarahkan ke fungsi view yang sesuai.  

### 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan
Menurut saya, tutorial 2 dari asdos sangat membantu dan penjelasannya jelas sehingga memudahkan dalam memahami langkah-langkah praktikum. Selain itu, asdos juga mengadakan Discord voice channel untuk menjelaskan lebih lanjut terkait tutorial, yang menurut saya sangat berguna.  

### 7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
<img width="1470" height="956" alt="Screenshot 1" src="https://github.com/user-attachments/assets/20a60466-c42d-46ed-a22a-cfd283b62354" />  
<img width="1470" height="956" alt="Screenshot 2" src="https://github.com/user-attachments/assets/973ab7b0-1f7a-49b8-9df0-77405887f583" />  
<img width="1470" height="956" alt="Screenshot 3" src="https://github.com/user-attachments/assets/5befa09e-dada-4a49-a9b1-41119603a1bf" />  
<img width="1470" height="956" alt="Screenshot 4" src="https://github.com/user-attachments/assets/9c095392-c4d3-4384-8cc1-9bd350847f4b" />  

---

## TUGAS 4: IMPLEMENTASI AUTHENTICATION, SESSION, DAN COOKIES PADA DJANGO

### 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya
Django **AuthenticationForm** adalah form bawaan Django yang digunakan untuk proses login pengguna. Form ini secara otomatis menyediakan field *username* dan *password*, serta melakukan validasi apakah kombinasi keduanya sesuai dengan data pengguna di database.

**Kelebihan:**
- Tidak perlu membuat form login dari nol, sehingga mempercepat pengembangan.  
- Sudah terintegrasi dengan sistem autentikasi bawaan Django.  
- Mendukung validasi otomatis (contoh: password salah, user tidak ditemukan).  

**Kekurangan:**
- Tampilan default masih sederhana, biasanya perlu dikustomisasi agar sesuai desain aplikasi.  
- Hanya cocok untuk kebutuhan autentikasi dasar; untuk login dengan email atau metode lain perlu modifikasi.  

### 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?
- **Autentikasi (authentication)** adalah proses memverifikasi identitas pengguna (mis. mencocokkan username dan password).  
- **Otorisasi (authorization)** adalah proses memverifikasi hak akses pengguna setelah identitasnya terverifikasi.  

Django mengimplementasikan keduanya dengan:  
- **User model** untuk menyimpan data pengguna.  
- **Auth views** (`authenticate()`, `login()`, `logout()`) untuk mengelola autentikasi.  
- **Decorator `@login_required`** untuk membatasi akses halaman hanya bagi pengguna yang sudah login.  

### 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
**Cookies**  
- *Kelebihan:* ringan, mudah diakses di client, cocok untuk menyimpan preferensi kecil.  
- *Kekurangan:* tersimpan di client (bisa dimanipulasi), rentan XSS, tidak cocok untuk data sensitif.  

**Session**  
- *Kelebihan:* lebih aman karena data disimpan di server, client hanya membawa `sessionid`.  
- *Kekurangan:* butuh penyimpanan server (DB/Redis), bisa membebani server bila jumlah user banyak.  

### 4. Apakah penggunaan cookies aman secara default? Risiko & bagaimana Django menanganinya
**Risiko:**  
- Bisa dipakai untuk tracking tanpa sepengetahuan user.  
- Bisa dicuri lewat serangan XSS.  
- Bisa dimodifikasi jika disimpan plaintext.  

**Penanganan Django:**  
- Menyimpan data sensitif di server via session, bukan langsung di cookie.  
- Melindungi form dengan CSRF token.  
- Melakukan hashing pada password agar tidak pernah disimpan plaintext.  

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
•	Pertama, saya membuat fitur login dan register menggunakan auth views yang sudah disediakan Django. Fitur logout juga diimplementasikan agar pengguna dapat keluar dari sesi. Dengan memanfaatkan fitur bawaan Django ini, saya bisa membangun aplikasi web dengan autentikasi dasar (login, register, logout) dengan lebih mudah dan aman.  
•	Kedua, saya membuat dua akun baru melalui halaman /register. Setelah itu, saya mencoba login dengan masing-masing akun secara bergantian. Setelah berhasil login, saya mengakses halaman /create untuk menambahkan tiga data dummy ke dalam model Product. Selanjutnya, saya melakukan logout, kemudian login kembali menggunakan akun yang berbeda untuk menguji konsistensi fitur autentikasi dan otorisasi.  
<img width="1247" height="734" alt="Screenshot 2025-09-24 at 04 58 09" src="https://github.com/user-attachments/assets/fd23c6bd-0a23-4782-bcbe-8f148f8230fc" />
<img width="1245" height="736" alt="Screenshot 2025-09-24 at 04 56 58" src="https://github.com/user-attachments/assets/99814992-2cf9-44da-9fe1-b5c13e41c14a" />
•	Ketiga, saya menghubungkan User dengan Product dengan menambahkan field user pada model Product menggunakan relasi ForeignKey. Dengan cara ini, setiap produk yang ditambahkan dapat terasosiasi dengan akun pengguna tertentu, sehingga produk dapat difilter berdasarkan pemiliknya.  
•	Keempat, saya menampilkan informasi last_login pada halaman web. Data ini diambil dari atribut bawaan model User yang dikelola Django. Untuk memastikan data tersimpan di sisi client, saya menggunakan cookies agar informasi waktu login terakhir bisa dilihat langsung dari browser pengguna. 

---

## TUGAS 5: DESAIN WEB MENGGUNAKAN HTML, CSS DAN FRAMEWORK CSS

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas (CSS Specificity) adalah:
1. **Inline style** → Gaya yang ditulis langsung di atribut (`style`) pada elemen HTML.
2. **ID selector** → Selector yang menggunakan ID elemen (`#id`).
3. **Class, attribute, dan pseudo-class selector** → Selector yang menggunakan kelas (Selector berdasarkan kelas (`.class`), atribut (`[type="text"]`), atau pseudo-class (`:hover, :focus`)
4. **Element dan pseudo-element selector** → Selector yang menargetkan tag HTML (`p, div`) atau pseudo-element (`::before, ::after`)
5. **Universal selector** → Selector (`*`) berlaku untuk semua elemen
Jika dua selector memiliki prioritas sama, maka aturan yang ditulis terakhir akan dipakai.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
**Responsive design penting** karena:  
- **Multi-device** → Website bisa dibuka di laptop, tablet, smartphone.  
- **User experience** → Tampilan nyaman, teks mudah dibaca, navigasi jelas.  
- **SEO advantage** → Google memberi ranking lebih tinggi untuk web mobile-friendly.  
- **Efisiensi** → Cukup 1 desain fleksibel tanpa bikin versi khusus mobile.  
**Contoh aplikasi yang menerapkan responsive design:** Amazon (tampilan adaptif di semua device).  
**Contoh aplikasi yang tidak menerapkan responsive design:** beberapa website lama instansi → tampilannya pecah/berantakan di HP.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- **Margin** → Mengatur jarak di luar elemen, yaitu jarak antar elemen di halaman.
- **Border** → Memberikan garis tepi pada elemen, berada di antara padding dan margin.
- **Padding** → Memberikan ruang di dalam elemen, yaitu jarak antara konten dan border. 

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**Flexbox**  
Flexbox adalah model layout satu dimensi yang dirancang untuk menata elemen dalam baris atau kolom. Flexbox memudahkan distribusi ruang dan penyelarasan item dalam sebuah container, bahkan ketika ukuran elemen tidak tetap atau dinamis.
**Kegunaan Flexbox:**
- Membuat layout menjadi fleksibel dan responsif.
- Menyelaraskan elemen secara vertikal dan horizontal dengan mudah.
- Mengubah urutan tampilan elemen tanpa perlu mengubah struktur HTML.
- Membuat navigasi bar yang responsif.
- Menyusun card layout yang fleksibel.
**Konsep Utama Flexbox:**
- Flex Container → elemen induk yang diberi (`display: flex`).
- Flex Items → elemen anak langsung di dalam flex container.
- Main Axis → sumbu utama (horizontal untuk `row`, vertikal untuk `column`).
- Cross Axis → sumbu yang tegak lurus dengan main axis.
  
**Grid Layout**  
Grid Layout adalah sistem layout dua dimensi yang memungkinkan penempatan konten dalam baris dan kolom secara bersamaan. Grid memberikan kontrol lebih besar dibanding Flexbox untuk menyusun halaman yang kompleks.
**Kegunaan Grid Layout:**
- Menyusun layout halaman yang kompleks dengan lebih mudah.
- Mengatur elemen dalam grid yang presisi.
- Membuat layout responsif yang dapat berubah signifikan pada breakpoint berbeda.
- Menangani layout dua dimensi lebih efisien dibanding Flexbox.
**Konsep Utama Grid:**
- Grid Container → elemen induk yang diberi (`display: grid`).
- Grid Items → elemen anak langsung di dalam grid container.
- Grid Lines → garis yang membatasi baris dan kolom.
- Grid Tracks → baris atau kolom di grid.
- Grid Cells → perpotongan antara baris dan kolom.
- Grid Areas → sekumpulan sel yang membentuk area tertentu.
  
### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Berikut langkah-langkah yang saya lakukan untuk mengimplementasikan fitur-fitur pada proyek ini:
**1. Menambahkan fungsi edit dan hapus produk**
Di file views.py, saya membuat fungsi edit_product dan delete_product. Fungsi ini memungkinkan pengguna untuk mengubah data produk atau menghapus produk secara langsung dari aplikasi.
**2. Mendesain halaman login, register, dan tambah produk**
Halaman-halaman ini didesain menggunakan CSS Flexbox dan Grid Layout agar tampilannya rapi dan responsif. Dengan Grid Layout, elemen akan menyesuaikan ukuran layar, sedangkan Flexbox membantu menyelaraskan konten secara horizontal dan vertikal.
**3. Mendesain halaman daftar produk**
Untuk menampilkan daftar produk, saya membuat file card_product.html dengan desain card yang menarik. Setiap produk ditampilkan dengan gambar, nama, harga, deskripsi, serta tombol Edit dan Delete. Desain ini menggunakan CSS Flexbox untuk menata tombol secara horizontal dan membuat tampilan lebih interaktif.
**4. Membuat navbar yang responsif**
Navbar dibuat menggunakan Flexbox agar elemen di dalamnya tersusun rapi dan dapat menyesuaikan ukuran layar. Dengan Flexbox, navbar bisa menyesuaikan posisi logo dan menu secara responsif pada berbagai ukuran layar.

**Kondisi navbar untuk versi mobile:**
<img width="401" height="66" alt="Screenshot 2025-09-30 at 18 54 45" src="https://github.com/user-attachments/assets/888c6708-1f7e-40a1-87a3-e77228afaa85" />

**Ketika tombol hamburger diklik:**
![Screenshot 2025-09-30 at 17 13 18](https://github.com/user-attachments/assets/711d09f1-52ab-4ec4-9eb2-c8feca1d12ed) />

**Kondisi navbar untuk versi desktop:**
<img width="1405" height="179" alt="Screenshot 2025-09-30 at 18 50 47" src="https://github.com/user-attachments/assets/bcb34554-1429-495c-a728-b1d84976b3b1" />

