
# Laporan Praktikum Minggu 2
Topik: Struktur System Call dan Fungsi Kernel 

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
System call adalah sebuah metode dimana program komputer meminta layanan tertentu dari sistem operasi.
System call juga menjadi penjaga agar setiap aplikasi di _user space_ melewati perizinan sebelum dapat mengakses sumber daya komputer.
Beberapa kategori utama system call yaitu manajemen proses, manajemen berkas, manajemen perangkat, pemeliharaan informasi, dan komunikasi.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

3. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. **Diagram Alur System Call**
   - Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
   - Gunakan draw.io / mermaid.
   - Simpan di:
     ```
     praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10

```

---

## Hasil Eksekusi
![Screenshot hasil](<screenshots/stracels1.jpeg>)
![Screenshot hasil](<screenshots/stracels2.jpeg>)
![Screenshot hasil](<screenshots/strace_e.jpeg>)
![Screenshot hasil](<screenshots/dmesg.jpeg>)


---

## Analisis
1. Hasil eksperimen ```strace``` dan ```dmesg``` dalam bentuk tabel observasi.


| Perintah | Keterangan Perintah | Output | Keterangan Output |
|:---:|:---|:----:|:-----|
| strace ls | Melacak system call yang dipanggil| execve()| Menjalankan program baru|
|   |    | mmap() | Memetakan file ke memori |
| | | brk() | mengubah ukuran segmen data |
| | | access() | mengecek hak akses file |
| | | openat() | membuka file atau direktori |
| | | fstat() | mengambil informasi file |
| | | close() | menutup file atau direktori|
| | | read() | membaca data dari file |
| dmesg tail -n 10 | digunakan untuk memeriksa atau mengontrol ring buffer kernel, perintah -n 10 akan membuatnya hanya menampilkan 10 output terakhir | [1687.711753] | merupakan waktu (detik) setelah komputer dinyalakan |
| | | [ 1687.711753] sd 0:0:2:0: [sdb] Mode Sense: 1f 00 00 08 | sistem mendeteksi perangkat penyimpanan baru |
| | | [ 1687.712031] sd 0:0:2:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA | disk memiliki cache baca/tulis aktif tapi tidak memiliki fitur DPO atau FUA|
| | |[ 1687.936211]  sdb: sdb1| Kernel menemukan partisi pertama pada disk |
| | | [ 1687.939070] sd 0:0:2:0: [sdb] Attached SCSI disk | perangkat penyimpanan dihubungkan ke sistem |
| | | [ 1688.119387] EXT4-fs (sdb1): mounted filesystem b9f0e455-8c03-483b-a0d6-629a47561fb9 r/w with ordered data mode. Quota mode: none. | partisi sdb1 dengan sistem file EXT4 berhasil di-mount dalam mode baca/tulis|
| | | [ 1689.263679] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/ipv4/netfilter/iptable_nat.ko" pid=2153 cmdline="/sbin/modprobe -q -- iptable_nat" | kernel memuat modul iptable.nat untuk fitur NAT di jaringan |
| | | [ 1689.367369] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netlink/netlink_diag.ko" pid=2173 cmdline="/sbin/modprobe -q -- net-pf-16-proto-4-type-16"| modul netlink_diag dimuat untuk mendiagnosis koneksi jaringan|
| | | [ 1691.930015] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netfilter/ipset/ip_set.ko" pid=2451 cmdline="/sbin/modprobe -q -- ipt_set" | modul ip_set dimuat untuk mengimpan daftar alamat IP|
| | | [ 1691.951106] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/netfilter/xt_set.ko" pid=2451 cmdline="/sbin/modprobe -q -- ipt_set" | modul xt_set dimuat untuk rule matching di iptables |
| | | [ 1691.982746] LoadPin: kernel-module pinning-excluded obj="/lib/modules/6.6.105+/kernel/net/ipv6/netfilter/ip6table_nat.ko" pid=2458 cmdline="/sbin/modprobe -q -- ip6table_nat" | modul ip6table_nat dimuat untuk NAT di jaringan IPv6|


   
2. Diagram alur system call


![diagram syscall](<screenshots/syscall-diagram.jpg>)



3. Ringkasan
   - Pentingnya _System Call_ Untuk Keamanan Sistem Operasi
  
       System call adalah suatu penghubung antara pengguna dan sistem operasi atau kernel space. Melalui _system call_, pengguna meminta layanan atau izin dari kernel agar perangkat dapat digunakan. Misalnya, pengguna dapat meminta izin ke kernel untuk membaca file, menempatkan memori, ataupun juga bisa menjadi perantara agar pengguna dapat berinteraksi dengan perangkat keras (hardware) tanpa memberikan akses penuh. Dari sisi keamanan, _system call_ adalah penghubung antara aplikasi dan kernel, tanpa ini, program pengguna bisa langsung mengakses sumber daya kernel, hal ini berbahaya karena oengguna bisa secara tidak sengaja memodifikasi sistem dan menyebabkan kerusakan. Dengan kata lain, _system call_ menjadi penghubung sekaligus penjaga yang memastikan setiap aplikasi melewati izin terlebih dahulu sebelum dapat mengakses ke inti sistem.
   - Bagaimana Sistem Operasi Memastikan Transisi _user-kernel_ Berjalan Aman
   
       Saat dalam _boot time_ atau saat komputer pertama kali dinyalakan. Hardware selalu mulai dalam mode kernel. Lalu sistem operasi dimuat dan memulai program pengguna di ruang pengguna (user space). Setiap _trap_ atau _interrupt_ terjadi, hardware akan beralih dari mode pengguna ke mode kernel. Sehingga, setiap kali sistem operasi mendapatkan kontrol terhadap komputer, akan selalu dalam mode kernel dan sistem selalu berpindah ke mode pengguna sebelum memberi kontrol ke program pengguna. _Interrupt & Trap_ adalah mekanisme yang digunakan untuk mengalihkan kontrol dari program pengguna ke mode kernel. Interrupt berasal dari luar CPU, misalnya hardware seperti keyboard, mouse, dan sebagainya. Sedangkan Trap merupakan interrupt yang disebabkan oleh instruksi dalam program itu sendiri. Misalnya, perintah read()
   , CPU akan membuat interrupt agar software melakukan perintah. Dual mode operasi ini memberi perlindungan ke sistem operasi terhadap kesalahan pengguna dan pengguna dari kesalahannya sendiri. Perlindungan ini dilakukan dengan cara menandai sejumlah instruksi berbahaya sebagai _privileged instructions_. Yang artinya, instruksi yang di tandai sebagai _privileged instructions_ hanya bisa dieksekusi atau dijalankan di mode kernel. Saat terdapat percobaan untuk menjalankan perintah ini di mode pengguna, hardware tidak akan menjalankan perintah itu dan menganggapnya sebagai ilegal dan melakukan _trap_ ke sistem operasi.
   - Contoh _system call_ yang sering digunakan

     | Perintah | Keterangan |
     |:-------:|:--------|
     | read() | Membaca data dari file descriptor|
     | write() | Menuliskan data ke file descriptor|
     | open() | Membuka file dan mengembalikan file descriptor untuk digunakan oleh proses|
     | close() | Menutup file descriptor yang sudah tidak digunakan|
     | fork() | Membuat proses baru (child process) yang merupakan salinan dari proses induk|
     | exec() | Menjalankan program baru, menggantikan proses yang sedang berjalan|
     | wait() | Menunggu _child process_ selesai dieksekusi|
     | exit() | Mengakhiri eksekusi program dengan status tertentu|
     | getpid() | Mengambil ID proses (Process ID) dari proses yang sedang berjalan|
     | mkdir() | Membuat direktori baru di sistem file|
     | rename() | Mengubah nama file|
     | time() | Mengambil waktu sistem saat ini|
     | alarm() | Mengatur timer untuk menghasilkan sinyal setelah waktu tertentu|
     | uname() | Mengambil informasi tentang sistem kernel|
     | chmod() | Mengubah izin akses file |
---

## Kesimpulan
- System Call berfungsi sebagai penghubung antara program pengguna dan kernel sekaligus penjaganya.
- Keamanan system call dijalankan dengan menandai berbagai perintah sebagai _privileged instructions_ yang membuat perintah tidak bisa dijalankan di mode pengguna
- Setiap permintaan dari program pengguna ke sistem operasi akan memicu trap atau interrupt yang membuatnya beralih ke mode kernel agar dapat menjalankan perintah

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?  
   **Jawaban:**  System call berfungsi sebagai penghubung agar aplikasi di program pengguna dapat meminta layanan tertentu dari sistem operasi seperti manajemen proses, manajemen file, manajemen perangkat, dan komunikasi antar-proses.
2. Sebutkan 4 kategori system call yang umum digunakan!  
   **Jawaban:**
   1. Manajemen proses, mengatur pembuatan, eksekusi, dan pemberhentian proses.
   2. Manajemen berkas, mengelola file seperti membuka, membaca, menulis, dan menutup file
   3. Manajemen perangkat, mengatur akses ke perangkat keras input dan output.
   4. Komunikasi, mengatur pertumaran data antarproses dan antarperangkat melalui jaringan.
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?  
   **Jawaban:**   Karena user program berjalan di dalam mode pengguna, sedangkan sejumlah perintah atau instruksi ditandai sebagai _privileged instructions_ yang dimana perintah ini tidak akan bisa di jalankan di mode pengguna, dan hanya bisa di jalankan di mode kernel sehingga user program tidak akan bisa melakukan perintah tersebut secara langsung.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Memahami berbagai perintah system call
- Bagaimana cara Anda mengatasinya?  Membaca dari berbagai sumber di internet

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
