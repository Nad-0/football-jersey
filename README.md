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