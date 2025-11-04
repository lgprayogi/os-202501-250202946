
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.  

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```
   
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
sudo adduser praktikan
sudo passwd praktikan
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
```

---

## Hasil Eksekusi
1. Experimen 1
   ![experimen 1](<screenshots/id.jpeg>)
2. Experimen 2
   ![experimen 2](<screenshots/top.jpeg>)
3. Experimen 3
   ![experimen 3](<screenshots/sleep.jpeg>)
4. Experimen 4
   ![experimen 4](<screenshots/pstree.jpeg>)

---

## Analisis
1. Experimen 1

   | Perintah | Output | Keterangan |
   |:-------:|:--------:|:----------|
   | `whoami` | upb | Perintah whoami berfungsi untuk menampilkan nama pengguna yang sedang aktif di terminal |
   | `id` | uid=1000(upb) gid=1000(upb) groups=1000 (upb), 4(adm), 20(dialout), 24(cdrom), 25(floppy), 27 (sudo), 29(audio), 38(dip), 44(video), 46 (plugdev), 100 (users), 107(netdev), 1001(docker) | Perintah `id` berfungsi untuk menampilkan informasi identitas pengguna. termasuk ID pengguna (UID), ID grup utama (GID), dan daftar grup lain yang diikuti pengguna |
   | `groups` | upb adm dialout cdrom floppy sudo audio dip video plugdev users netdev docker | Perintah `group` digunakan untuk menampilkan daftar grup yang diikuti pengguna |

2. Experimen 2

  A. Perintah `ps aux` digunakan untuk menampilkan informasi tentang semua proses yang sedang berjalan di sistem, termasuk semua pengguna dan proses yang tidak terhubung ke terminal.

   Penjelasan output:

   | Kolom | Nama | Keterangan |
   | :-----:|:----:|:---------|
   | USER| User | Pengguna yang menjalankan akses |
   | PID | Process ID | Nomor identifikasi unik milik proses, digunakan untuk mengelila atau menghentikan proses |
   | %CPU | CPU usage | Persentase penggunaan CPU oleh proses saat ini |
   | %MEM | Memory usage | Persentase penggunaan RAM oleh proses |
   | VSZ | Virtual Memory Size | Total memori virtual yang dialokasikan untuk menggunakan proses|
   | RSS | Resident Set Size | Jumlah RAM fisik yang digunakan oleh proses|
   | TTY | Terminal | Terminal asal proses |
   | STAT | Status | Status proses, misal R = Running, S = Sleeping |
   | START | Start time | Waktu saat proses dimulai|
   | TIME | CPU Time | Total waktu CPU yang telah digunakan proses sejak berjalan|
   | COMMAND | Command | Perintah yang menjalankan proses tersebut|

  B. Perintah `top -n 1` 
  
   Perintah `top` digunakan untuk menampilkan informasi real-time tentang proses yang berjalan dan penggunaan sumber daya sistem, opsi `-n` = number of iteration. Artinya, berapa kali `top` melakukan refresh. Jadi `-n 1` hanya akn membuat perintah `top` dieksekusi satu kali tanpa refresh lagi setelahnya.

  Penjelasan output:

  | Kolom | Nama | Keterangan| 
  |:------:|:-----:|:---------|
  | PID | Process ID | Nomor identifikasi unik milik proses, digunakan untuk mengelola atau menghentikan proses.|
  | USER | User | Pengguna yang menjalankan akses |
  | PR | Priority | Prioritas proses, semakin rendah angka = prioritas lebih tinggi |
  | NI | Nice value | Nilai prioritas tambahan|
  | VIRT | Virtual memory | Total memori virtual yang dialokasikan proses |
  | RES | Resident memory | Jumlah RAM fisik yang digunakan proses |
  | SHR | Shared memory | Memori yang dapat dibagi dengan proses lain |
  | S | State | Status proses R = Running, S= Sleeping, T= Stopped. |
  | %CPU | CPU Usage | Persentase CPU yang digunakan proses saat ini |
  | %MEM | Memory Usage | Persentase penggunaan RAM oleh proses |
  | TIME+ | CPU time | Total waktu CPU yang dipakai sejak proses dimulai |
  | COMMAND | Command | Perintah yang menjalankan proses tersebut |

3. Eksperimen 3
   
   Perintah `sleep 1000 &`
   
   Perintah `sleep` digunakan untuk menghentikan sementara skrip atau eksekusi perintah selama jangka waktu tertentu
   angka `1000` setelah perintah `sleep` berarti jangka waktu tersebut adalah 1000 detik dan simbol `&` berfungsi untuk mengirim  perintah ke background, artinya perintah akan berjalan secara independen dari perintah utama dan memungkinkan pengguna untuk tetap berinteraksi dengan terminal dan menjalankan prrintah lain saat perintah `sleep` tetap berjalan.

  Perintah `ps aux | grep sleep`
  
  Perintah `ps aux` digunakan untuk menampilkan semua proses yang sedang berjalan di sebuah komputer, `|` (pipe) akan mengambil output dari perintah sebelah kiri yaitu `ps aux` untuk digunakan sebagai input untuk perintah sebelah kanan yaitu `grep sleep` yang berfungsi untuk menyaring (filter) output dari `ps aux` agar yang ditampilkan hanya proses yang memiliki kata kunci 'sleep'.

  Output:

  ``` bash
upb            67 0.0 0.0 11164 928 tty1    S   18:51 0.00 sleep 1000
```

Perintah kill <PID>

  perintah `kill` akan mengakhiri suatu proses dengan process ID(PID) nya. Output diatas menunjukan jika perintah sleep memiliki PID yaitu 67. `kill 67` akan mengakhiri proses tersebut.

  Perintah `pstree -p | head -20`
  digunakan untuk menampilkan semua proses yang berjalan dalam struktur pohon, `head -20` hanya akan menampilkan 20 baris pertamanya.

Output:

```bash
init(Ubuntu)(1)-+-SessionLeader(8)---bash(9)-+-head(74)
                |                            `-pstree(73)
                |-init(5)---{init}(6)
                `-{init(Ubuntu)}(7)
```

 dapat dilihat bahwa awal dari cabang adalah init(Ubuntu)(1) yang merupakan proses utama yang bertanggung jawab memulai dan mengelola semua proses lain dalam sistem.
  
---

## Tugas

1. Hierarki proses dalam bentuk diagram pohon

```bash
init(Ubuntu)(1)-+-SessionLeader(8)---bash(9)-+-head(74)
                |                            `-pstree(73)
                |-init(5)---{init}(6)
                `-{init(Ubuntu)}(7)
```

2. Hubungan antara user management dan keamanan sistem Linux

   User management adalah hal yang sangat penting untuk keamanan sistem linux, karena dengan memanajemen pengguna, mengatur akses pengguna atas perintah dan sumber daya komputer akan membuat lingkungan sistem lebih aman dan terkendali.



## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?   
   **Jawaban:**  `init` atau `systemd` bertanggung jawab untuk mengelola proses boot, memulai dan menghentikan layanan, dan menangani penghentian sistem.
2. Apa perbedaan antara `kill` dan `killall`? 
   **Jawaban:**  perintah `kill` hanya akan menghentikan satu program berdasarkan process ID (PID) nya, sementara kill all menghentikan semua proses dengan nama yang cocok sekaligus.
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?
   **Jawaban:**  user `root` memiliki hak istimewa di sistem linux karena bertindak sebagai administrator utama (superuser) yang memiliki akses ke semua perintah dan sumber daya sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
