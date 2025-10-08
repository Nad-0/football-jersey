Nama = Go Nadine Audelia
NPM = 2406348774
Kelas = PBP C

TUGAS 2
Tautan menuju aplikasi PWS = https://pbp.cs.ui.ac.id/go.nadine/football-jersey-shop

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
- Membuat sebuah proyek Django baru.
Untuk membuat proyek django baru, pertama-tama saya membuat sebuah folder baru yang berjudul football-jersey-shop. Kemudian saya mengaktifkan virtual environment,menginstal beberapa requirements, dan membuat proyek barunya. Selanjutnya saya membuat file .env.prod dan memodifikasi sedikit file .env serta settings.  
- Membuat aplikasi dengan nama main pada proyek tersebut.
Untuk tugas list yang ini saya hanya perlu melanjutkan step sebelumnya dengan membuat dan mendaftarkan aplikasi main dalam proyek football-jersey-shop. Untuk mengisi web maka perlu membuat folder templates dan file main.html, di file inilah saya menuliskan sejumlah kode termasuk nama aplikasi, nama, dan kelas saya untuk menghias tampilan web.
- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
Tahap ini dilakukan dengan membuka file urls.py di dalam folder proyek. Selanjutnya, saya mengimpor fungsi include dan menambahkan rute url.
- Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
Untuk langkah ini, saya tinggal membuka file model yang telah ada dan menuliskan kode untuk atribut-atribut yang diminta. Kemudian, saya melakukan migrasi model agar django dapat mengetahui perubahan model yang terbaru.
- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Saya membuka berkas views dan menuliskan beberapa baris kode dan function agar kode yang saya tuliskan di main.html dapat terlihat.
- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Saya membuat file urls di folder main, lalu mengimpor path dan show_main serta menuliskan app_name dan urlpatterns.
- Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Saya login dengan akun SSO ke web PWS, lalu saya menekan pilihan create new project. Saya menamai project baru itu dengan football-jersey-shop. Pada tab environs, saya memilih raw editor dan memodifikasi isinya. Setelah selesai, saya menekan tombol update all variables. Selain itu, saya juga menambahkan url deployment PWS di file settings.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Link bagan = https://www.canva.com/design/DAGyf77ZqPM/2X6vdkJyYc3IeTmjARU3WA/edit?utm_content=DAGyf77ZqPM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
Penjelasan: Ketika client mengirimkan request, maka django akan menerima request tersebut dan mencoba mencocokkan di urls.py. Jika tidak cocok, maka Django menampilkan 404 Not Found. Namun jika cocok, Django akan meneruskan request itu ke views.py. Views.py melakukan tindakan berupa pemanggilan models.py untuk mengambil data sesuai request. Setelah mendapatkan data dari models.py, views akan merender berkas HTML sesuai dengan data yang telah didapat. Terakhir, view akan mengirim respon yang dapat berbentuk http, json, file, ataupun redirect ke client.    

3. Jelaskan peran settings.py dalam proyek Django!
Settings.py mengatur segala cara kerja proyek Django. Settings memiliki status debug, installed apps, dapat memproses request dan respon, mengatur lokasi template html, dan menghubungkan aplikasi dengan sistem.  

4. Bagaimana cara kerja migrasi database di Django?
Django tidak dapat langsung mengubah database jika ada perubahan pada model sehingga migrasi sangat diperlukan dalam proses ini. Django perlu membuat file migrasi yang berisi perubahan database, kemudian menggunakan intruksi python manage.py migrate untuk menerapkan perubahan terbaru ke database.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django digunakan sebagai permulaan karena Django memiliki banyak keunggulan yang dapat mempermudah pemula seperti saya. Keunggulan pertama adalah django dirancang untuk mempercepat pengembangan perangkat lunak. Banyak sekali fitur bawaan Django yang membantu untuk mempercepat sebuah ide menjadi aplikasi yang berjalan. Django juga memiliki fleksibilitas yang besar karena bisa digunakan di berbagai jenis aplikasi web, sehingga mahasiswa tidak terbatas pada satu domain saja dan menjadi mengenali banyak jenis aplikasi web.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tidak ada feedback dari saya. Tutorial 1 dapat saya cukup pahami dan asisten dosen juga telah bekerja dengan baik.


TUGAS 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan untuk kepentingan komunikasi antara user dan sistem. Dengan menggunakan data delivery, informasi user dapat dikirimkan dan diproses oleh server. Data delivery juga memastikan keamanan data yang berpindah melalui enkripsi dan autentikasi. Terakhir, data delivery memungkinkan integrasi dengan layanan pihak ketiga.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dikarenakan beberapa alasan yang sama dengan alasan mengapa JSON lebih populer. JSON lebih sederhana dan efesien daripada XML. JSON menggunakan format key value sehingga lebih mudah dipahami. Selain itu dibandingkan XML, JSON memiliki banyak dukungan dan integrasi dengan JavaScript dan berbagai framework.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() dibutuhkan karena berperan penting untuk validasi data yang dikirimkan form. Validasi data sangatlah penting dalam menjaga konsistensi data. Validasi data menghindarkan dari masuknya data tidak sesuai ke database yang dapat menyebabkan error.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Dibutuhkan csrf_token untuk melindungi aplikasi dari serangan Cross-Site Request Forgery. CSRF adalah serangan dari penyerang yang memanfaatkan sesi user yang sedang aktif untuk mengirimkan request berbahaya tanpa sepengetahuan user. Jika csrf_token tidak ditambahkan, maka penyerang dapat membuat halaman berbahaya yang secara otomatis mengirimkan request ke server menggunakan kredensial pengguna yang sudah login, misalnya melakukan perubahan data dengan nama korban.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
Pertama-tama, saya membuat file base.html yang berfungsi sebagai template dasar yang dapat digunakan sebagai kerangka umum. Kemudian memastikan agar base.html terdeteksi sebagai template dan membuat main.html extends base.html. Tahap kedua, saya membuat forms.py pada folder main untuk menerima data baru. Selanjutnya, saya menambahkan beberapa import dan fungsi di views.py. Saya membuka main.html dan menambahkan kode yang menampilkan data product serta tombol add. Membuat file create_product dan product_detail lalu menambahkan url proyek ke csrf_trusted_origins. Tahap ketiga adalah mengembalikan data dalam bentuk XML dan JSON. Saya mengimport HttpResponse dan Serializer di views.py, lalu membuat fungsi show_xml dan show_json serta mengimpor fungsi yang telah dibuat tadi di urls.py dan menambahkan path agar dapat mengakses fungsinya. Tahap empat adalah mengembalikan data berdasarkan ID. Caranya adalah dengan menambahkan dua fungsi tentang show by id di file views. Lalu di views.py mengimpor fungsi tadi dan menambahkan path ke url. 

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada feedback dari saya. Semuanya udah bagus aja.

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md!
https://drive.google.com/drive/folders/1v2IRwDMkuyOaWeBDtMXTCxlVP0VaA520?usp=sharing


TUGAS 4
1.  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm merupakan form yang disediakan oleh Django untuk membantu developer mengurus proses login user dengan memeriksa kecocokan username dan password. Kelemahannya adalah hanya menyediakan login lewat username dan password, sehingga dev harus melakukan modifikasi jika ingin login dengan cara lain. Kelebihannya adalah mudah digunakan karena merupakan form bawaan Django serta dapat mempercepat pengembangan aplikasi dengan login standar.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses memverifikasi user yang login, sedangkan autorisasi adalah proses untuk memverifikasi mengenai apakah user mempunyai akses ke suatu hal. Untuk autentikasi, Django telah menyediakannya di django.contrib.auth. yang memiliki 3 komponen utama. Tiga komponen tersebut adalah user model, function authenticate() serta login() dan logout(). User model menyimpan data akun, authenticate() untuk validasi kredensial, dan komponen terakhir untuk mengatur sesi login serta logout. Untuk otorisasi, Django telah menyediakan permission dan group system. Ada 3 level otorisasi, yang pertama adalah permission yang dapat menambahkan, menghapus, dan mengubah objek. Kedua adalah group yang merupakan sekumpulan permission. Terakhir adalah custom decorator yang berfungsi untuk membatasi akses view.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session menyimpan data di server. Kelebihan session adalah lebih aman karena data penting disimpan oleh server, ukuran data yang disimpan lebih besar dan fleksibel, dan tidak mudah dimodifikasi oleh client. Kekurangan session adalah dapat membebani server jika user terlalu banyak, session bisa hilang jika user logout, dan session harus kadaluarsa agar tidak menumpuk. Cookies adalah data yang disimpan di browser user. Kelebihan cookies adalah data tetap tersimpan walaupun server direstart, tidak membebani server karena data tersimpan di client, dan mudah digunakan karena browser otomatis mengirim cookie ke server setiap request. Kekurangan cookies adalah ukuran data yang tersimpan terbatas, kurang aman karena biasanya tidak dienkripsi, dan tidak cocok untuk data sensitif karena client punya akses penuh ke cookie.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies tidak terlalu aman secara default. Cookies adalah data yang tersimpan di browser sehingga ada potensi terjadinya pencurian data, manipulasi data, dll. Django menangani hal tersebut dengan menyediakan beberapa konfigurasi bawaan yang memperkuat keamanan cookies. Yang pertama adalah fitur Secure Cookie yang berarti cookie hanya bisa dikirimkan lewat HTTPS sehingga tidak bisa disadap di HTTP. Kedua, HttpOnly Cookie yang berfungsi agar cookie tidak bisa diakses lweat JavaScript untuk mencegah pencurian cookie. Ketiga, SameSite Attribute yang membatasi cookie dikirim ke domain lain untuk mengurangi risiko CSRF. Keempat, CSRF Protection artinya Djangi mempunyai CSRF token untuk melindungi form POST. Terakhir adalah fitur session di server side sehingga walaupun cookie terbaca tetapi isi datanya tidak terekspos.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
Pertama-tama, saya mengimport UserCreationForm dan messages di views.py serta menambahkan fungsi register di views. Selanjutnya saya membuat file register.html. dan menambahkan path urlnya. Untuk fungsi login, saya mengimport authenticate, login, dan AuthenticationForm. Lalu membuat fungsi login_user, membuat file login.html, dan menambahkan path url login. Untuk logout, saya mengimport logout dari django.contrib.auth, membuat fungsi logout_user di views.py , menambahkan kode untuk logout di main.html, dan menuliskan path url dalam urlpatterns. 
-  Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
Saya mengaktifkan env lalu run server terlebih dahulu. Kemudian saya tinggal membuat dua akun user dan menambahkan tiga produk pada masing-masing akun.
- Menghubungkan model Product dengan User.
Saya mengimport User di models.py, memodifikasi model Product dengan menambahkan variable user, lalu melakukan migrasi. Kemudian syaa mengubah kode di fungsi create_product, memodifikasi show_main, menambahkan tombol filter My dan All di main.html, dan menampilkan nama author di product_detail.html.
- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
Untuk menampilkan status login atau logout, saya mengimport HttpResponseRedirect, reverse, dan datetime, memodifikasi fungsi login_user agar dapat menyimpan cookie bernama last_login, memodifikasi fungsi show_main, mengubah fungsi logout_user untuk menghapus cookie last_login setelah logout, dan menambahkan kode untuk menampilkan last login di main.html.

TUGAS 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas ditentukan oleh tingkat kekhususan dan urutan pembacaan. Selector dengan prioritas tertinggi adalah inline style yang ditulis langsung pada elemen dengan atribut style. Setelah itu, selector dari ID selector memiliki prioritas lebih tinggi dibanding class, pseudo-class, atau atribut selector. Di bawahnya, terdapat element selector dan pseudo-element yang tingkat kekhususannya lebih rendah. Universal selector memiliki prioritas paling rendah. Jika dua selector memiliki tingkat kekhususan yang sama, maka selector yang ditulis paling akhir dalam urutan pembacaan akan dipakai. 

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design memastikan tampilan dan fungsi dapat menyesuaikan dengan berbagai ukuran layar dan perangkat, pengalaman pengguna lebih baik, dan navigasi lebih mudah. Contoh aplikasi yang sudah menerapkan responsive design adalah website emas UI karena sudah dapat menyesuaikan dengan berbagai ukuran layar. Sedangkan, contoh aplikasi  web yang belum menerapkan responsive design adalah pacil web service karena tampilan belum dapat menyesuaikan dengan berbagai ukuran.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah ruang transparan di luar elemen yang berfungsi untuk menciptakan jarak antar elemen di halaman. Padding adalah ruang transparan di dalam elemen yang memberi jarak antara konten dengan garis tepinya. Border adalah garis visual yang membungkus konten dan padding. Dalam CSS, ketiga properti ini dapat diimplementasikan menggunakan properti shorthand misal padding: 20px atau properti longhand misal margin-top: 15px.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
CSS Flexbox dan Grid adalah dua model tata letak modern. Flexbox mengatur item dalam satu dimensi. Grid dirancang untuk tata letak dua dimensi. Flexbox cocok untuk komponen seperti menu navigasi dan perataan konten di dalamnya. Grid untuk membangun kerangka halaman web yang terstruktur seperti header, sidebar, dan konten utama. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step!
- Implementasikan fungsi untuk menghapus dan mengedit product.
Untuk mengedit product, Saya membuat fungsi edit_product , membuat file edit_product.html di folder main, kemudian saya mengimpor fungsi tersebut di urls.py,  menambahkan path edit_product ke urlpatterns, lalu terakhir saya memodifikasi main.html agar button edit bisa muncul. Untuk menghapus product, saya membuat fungsi delete_product terlebih dahulu, lalu mengimpor dan menambahkan path delete_product di views.py, terakhir saya memperbaharui kode di main.html agar button delete bisa muncul.
- Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
Saya memperbaharui file login.html, register.html, create_product.html, edit_product.html, dan product_detail.html agar tampilannya jadi menarik.
-  Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
Pertama-tama saya memilih sebuah gambar dan mengganti namanya menjadi no-news.png, lalu saya menempatkan gambar itu di folder image yang ada di dalam folder static. Lalu, saya memodifikasi file main.html agar tulisan dan gambar saat tidak ada product bisa terlihat.
-  Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card!
Saya mengimplementasikan hal tersebut melalui file card_product.html
- Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
Saya membuka file main.html adan menambahkan kode tentang dua button tersebut di loop product_list.
- Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
Saya membuat file baru bernama navbar.html di folder templates. Saya mengisi file tersebut dengan kode navbar, kemudian menuliskan include navbar.html di main.html.

TUGAS 6
1. Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request bersifat memblokir karena setelah program mengirimkan sebuah permintaan maka akan berhenti total dan menunggu hingga respons diterima sebelum dapat melanjutkan ke tugas berikutnya. Sedangkan, asynchronous request tidak bersifat memblokir karena setelah mengirim permintaan, program dapat langsung melanjutkan untuk mengerjakan tugas-tugas lain tanpa harus menunggu respons datang.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
Alur kerja AJAX di Django dimulai dari aksi user di web yang memicu event listener pada JavaScript. Skrip ini kemudian mencegah perilaku default browser seperti reload halaman dan mengirimkan permintaan HTTP di latar belakang menggunakan fetch() ke sebuah URL endpoint spesifik yang telah terdaftar di urls.py Django. Untuk keamanan, JavaScript akan menyertakan CSRF token yang diambil dari halaman. Setelah diterima oleh server, Django akan meneruskan permintaan ke fungsi view yang sesuai. View ini kemudian memproses data yang dikirim dan mengemas hasilnya ke dalam format data menggunakan JsonResponse. Lalu, respons JSON dikirim kembali ke browser, di mana JavaScript akan menerimanya dan menggunakan data tersebut untuk memanipulasi DOM serta memberikan pembaruan instan pada halaman tanpa perlu mereloadnya sama sekali.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
AJAX di Django membuat website terasa lebih cepat dan modern karena hanya memperbarui bagian halaman yang perlu saja, tanpa reload semuanya. Hal ini membuat transfer data lebih hemat dan server lebih ringan serta cocok untuk fitur interaktif. Sebaliknya, render biasa memuat ulang seluruh halaman dan lebih cocok untuk halaman statis yang sederhana.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Pertama-tama pastikan enkripsi menggunakan HTTPS untuk melindungi data kredensial. Selain itu, perlu menyertakan token CSRF dalam setiap header request AJAX untuk mencegah serangan pemalsuan permintaan. Terakhir, selalu gunakan form bawaan Django seperti AuthenticationForm dan UserCreationForm untuk melakukan validasi yang aman di server. 

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX meningkatkan pengalaman pengguna dengan membuat website terasa jauh lebih cepat dan responsif. Hal ini dikarenakan AJAX dapat memperbarui konten halaman yang diperlukan saja tanpa memuat ulang seluruh halaman. 