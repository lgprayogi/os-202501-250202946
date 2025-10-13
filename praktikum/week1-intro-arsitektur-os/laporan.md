
# Laporan Praktikum Minggu 1
Topik: "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Lintang Galih Prayogi 
- **NIM**   : 250202946 
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menjelaskan peran sistem operasi dalam arsitektur komputer.
2. Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
3. Membandingkan model arsitektur OS (monolithic, layered, microkernel).
4. Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).
---

## Dasar Teori
1. _Operating System_ adalah perangkat lunak utama pada sebuah komputer yang mengelola seluruh sumber daya pada perangkat lunak dan perangkat keras, serta menyediakan antarmuka bagi pengguna untuk mengoperasikan komputer.
2. _Kernel_ merupakan program komputer yang menjadi inti dari sebuah sistem operasi komputer, dengan kontrol terhadap segala hal atas sistem tersebut.
3. _System Call_ adalah sebuah mekanisme bagi program aplikasi untuk meminta layanan dari sistem operasi.
---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---
## Hasil Eksekusi

![screenshots](<screenshots/ss_tugas.png>)

---

## Analisis
- **Analisa perintah**
  1. ```uname -a``` menampilkan informasi lengkap sistem operasi dan kernel linux yang berjalan.
  2. ```whoami``` menampilkan nama pengguna yang sedang login.
  3. ```lsmod | head``` menampilkan daftar modul kernel yang sedang dimuat, perintah ```head``` akan membuat hanya 10 baris pertama yang di tampilkan.
  4. ```dmesg | head``` menampilkan pesan log sistem (pesan dari kernel) sejak komputer dinyalakan atau sistem di-boot.
- Hubungan dengan teori:
  1. Kernel mengelola informasi sistem (uname), pengguna (whoami), modul perangkat keras (lsmod), serta proses inisialisasi dan log sistem sejak komputer dinyalakan (dmesg).
  2. System call memungkinkan perintah di user space melalui Shell untuk berinteraksi aman dengan kernel space tanpa langsung mengakses hardware.
  3. Kernel dan user di sistem operasi ini memiliki akses yang berbeda terhadap sumber daya komputer. User memiliki akses yang lebih sedikit dibandingkan kernel yang bisa langsung berkomunikasi dengan hardware.
  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
  • Hasil percobaan perintah di Linux akan berbeda jika dlakukan di Windows, karena perintah seperti ```uname, lsmod, dmesg``` adalah perintah khusus linux yang dimana Windows tidak mendukung untuk menjalankan perintah itu. Secara umum, 
Windows membatasi akses pengguna terhadap sistem inti dan kernel demi menjaga keamanan sistem itu sendiri, sehingga interaksi pengguna dilakukan melalui antarmuka tertentu. Sementara itu, Linux lebih membebaskan pengguna untuk mengakses dan memodifikasi sistem melalui terminal.
---

## Kesimpulan
 1. Linux memiliki arsitektur berlapis yang memisahkan ruang pengguna (user space) dan kernel.
 2. Kernel menjadi perantara antara sistem aplikasi dengan hardware melalui system call.
 3. Perintah seperti ```uname, whoami, lsmod, dmesg``` berfungsi untuk menampilkan informasi tentang perangkat dan user.
---

## Ringkasan
ARSITEKTUR SISTEM OPERASI KOMPUTER

 A. MODEL ARSITEKTUR OS
  1. MONOLITHIC KERNEL
Dalam pendekatan monolitik  seluruh sistem operasi berjalan sebagai satu program di mode kernel. Sistem ini ditulis sebagai sekumpulan prosedur digabung menjadi satu program biner besar. Saat digunakan, semua prosedur di dalam sistem dapat memanggil satu sama lain jika prosedur tersebut menyediakan perhitungan yang dibutuhkan. Kemampuan untuk memanggil semua prosedur yang dibutuhkan sangat efisien, namun mempunyai ribuan prosedur yang bisa memanggil satu sama lain tanpa batasan bisa mengakibatkan sistem yang sulit dikendalikan dan sulit dimengerti. Selain itu jika salah satu prosedur _crash_ akan mengakibatkan semua prosedur ikut gagal. Meski begitu kecepatan dan efisiensi monolitik kernel menjadi jawaban mengapa kita masih melihat struktur ini digunakan di sistem operasi unix Linux dan Windows. 
  2. MICROKERNEL
Sekitar tahun 1980 peneliti di Carnegie Mellon University mengembangkan sebuah sistem operasi bernama Mach yang menggunakan pendekatan mikrokerneL. Metode ini menyusun sistem operasi dengan menghapus komponen-komponen yang kurang dibutuhkan dari kernel dan menerapkannya ke program tingkat pengguna yang berada di ruang terpisah. Hasilnya adalah kernel yang lebih kecil, salah satu keuntungannya yaitu membuat perluasan sistem operasi menjadi lebih mudah dari sebelumnya. Semua layanan baru ditambahkan ke ruang pengguna dan tidak memerlukan modifikasi kernel dan ketika kernel memang perlu dimodifikasi, perubahannya cenderung lebih kecil karena microkernel adalah kernel yang lebih kecil. Microkenel juga memberikan keamanan dan keandalan yang lebih baik karena sebagian besar layanan bekerja sebagai proses pengguna dan bukan proses kernel. Jika salah satu layanan gagal, operasi lain akan tetap berjalan. Contoh yang paling dikenal adalah Darwin, komponen kernel dari sistem operasi Mac OS dan iOS.  
  3. LAYERED ARCHITECTURE
Sebuah sistem bisa dibuat modular lewat banyak cara, salah satu metodenya yaitu layered approach dimana sistem operasi dipisah menjadi beberapa layers(lapisan) layer bawah atau layer 0 adalah hardware. Layer yang tertinggi adalah interface pengguna. Sebuah lapisan sistem operasi adalah implementasi dari objek abstrak yang terdiri dari data dan operasi yang bisa memanipulasi data tersebut. Misalnya lapisan M, terdiri dari struktur data dan serangkaian fungsi yang dapat dipanggil oleh lapisan tingkat yang lebih tinggi. Lapisan M, pada gilirannya, dapat memanggil operasi pada lapisan tingkat yang lebih rendah. Keuntungan utama dari layer approach adalah kesederhanaan konstruksi dan lapisannya dipilih sehingga masing-masing hanya menggunakan fungsi dan layanan dari lapisan yang lebih rendah. lapisan pertama dapat _debug_ tanpa khawatir dengan sistem sisanya, karena lapisan ini hanya menggunakan perangkat keras dasar untuk dapat dijalankan fungsinya. Setelah lapisan pertama selesai di _debug_ fungsi yang benar dapat diasumsikan saat lapisan kedua di _debug_ dan seterusnya. Jika ditemukan kesalahan saat _debugging_ lapisan tertentu, kesalahan tersebut pasti ada di lapisan itu. Contoh sistem operasi yang menggunakan adalah the OS.

 B. ANALISIS
Manakah yang paling relevan untuk teknologi modern?
Dalam prakteknya sangat sedikit sistem operasi yang terpakumengadopsi satu struktur. Sebaliknya mereka menggabungkan berbagai struktur menghasilkan sistem hibrida yang menangani masalah performa keamanan dan juga kegunaan sebagai contohnya Linux bersifat monolitik karena memiliki seluruh sistem operasi dalam suatu ruang alamat memberikan performa yang sangat efisien namun Linux juga modular sehingga fungsi baru bisa ditambahkan ke kernel secara dinamis Windows sebagian besar juga monolitik karena alasan performa tetapi tetap mempertahankan beberapa perilaku khas sistem mikrokernel termasuk mendukung subsistem terpisah dikenal sebagai operating system personalitis yang berjalan sebagai proses mode pengguna

 C. REFERENSI
1. Abraham Silberschatz, Peter Baer Galvin, Greg Gagne. Operating System Concepts, 10th Edition, Wiley, 2018.
2. Andrew S. Tanenbaum, Herbert Bos. Modern Operating Systems, 4th Edition, Pearson, 2015.
   
## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.
   **Jawaban:** Fungsi utama sistem operasi yaitu manajemen sumber daya, manajemen proses, dan antarmuka pengguna.
2. Jelaskan perbedaan antara kernel mode dan user mode.
   **Jawaban:** Perbedaan paling mendasar antara kernel mode dan user mode adalah akses dan izin mereka terhadap sumber daya sistem. Kernel memiliki akses penuh terhadap sistem sedangkan user hanya diberi akses dan izin yang terbatas.
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
   **Jawaban:** Contoh OS dengan arsitektur monolithic yaitu Linux dan Windows, contoh OS dengan arsitektur microkernel yaitu QNX, MINIX, dan Mach
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  **Jawaban:** Cara mengoperasikan git
- Bagaimana cara Anda mengatasinya?
  **Jawaban:** Mencari tutorial di internet dan berdiskusi dengan orang lain.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
