
# Laporan Praktikum Minggu 3
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : Lintang Galih Prayogi 
- **NIM**   : 250202946 
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
2. Menggunakan chmod dan chown untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
pwd
ls -l
cd /tmp
ls -a
echo "Hello <Lintang><250202946>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/sscmdweek4.jpeg>)

---

## Analisis
1. Eksperimen 1

   | Perintah | Output | Keterangan |
   |:-------: | :-----: | :-------- |
   | ```pwd``` | ```/root``` | Perintah pwd (Print Working Directory) berfungsi untuk menampilkan direktori saat ini. ```/root``` berarti saat ini user sedang berada di direktori /root|
   | ```ls -l``` | ```total 0``` | perintah ```ls -l``` berfungsi untuk menampilkan seluruh folder dan file dalam direktori saat ini. ```total 0``` berarti isi direktori saat ini kosong |
   | ```cd /tmp``` | - | perintah ini berfungsi untuk berpindah direktori (Change Direktori). ```tmp``` berarti berarti temporary directory yang akan hilang secara otomatis saat sistem reboot|
   | ```ls -a``` | ```. ..``` | perintah ini berfungsi untuk menampilkan semua file dan folder, termasuk yang tersembunyi. Output menunjukan jika direktori saat ini kosong |


2. Eksperimen 2

```bash
root@DESKTOP-NM5Q219:/tmp# cat /etc/passwd | head -n 5
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
```


Penjelasan isi file dan strukturnya:


| User | UID | GID | Home | Shell | Keterangan |
|:-----|:----:|:----:|:---|:----|:----|
|`root`| 0 | 0| `/root` | `/bin/bash` | Administrator sistem|
|`daemon`| 1 | 1 | `/usr/sbin` | `/usr/sbin/nologin` | Akun untuk menjalankan daemon sistem|
|`bin` | 2 | 2 | `/bin` | `/usr/sbin/nologin` | Akun untuk program biner sistem |
|`sys`| 3 | 3 | `/dev` | `/usr/sbin/nologin` | Akun sistem internal|
|`sync`| 4 | 65534 | `/bin` | `/bin/sync` | Digunakan untuk sinkronisasi disk manual |

3. Eksperimen 3

   a. Output sebelum perintah `chmod`:
   `-rw-r--r-- 1 root root 27 Oct 27 18:10 percobaan.txt`
   
   b. Output sesudah perintah `chmod`:
   `-rw------- 1 root root 27 Oct 27 18:10 percobaan.txt`
   
Penjelasan:
| output | Keterangan |
| :----: | :------- |
| - | file biasa (bukan folder) |
| rw- | owner (root) bisa membaca dan menulis |
| r-- | group (root) hanya bisa membaca |
| r-- | selain owner dan group juga hanya bisa membaca |

Keterangan ini juga bisa dilihat dari gambar berikut:

![Permission Code](<screenshots/Permission.png>)

1. Karakter pertama: tipe file
   - (-) : file biasa
   - d : direktori
2. Sembilan karakter berikutnya terbagi menjadi 3:
   - rwx → owner
   - rwx → group
   - rwx → others
3. Setiap huruf mempunyai arti:
   - r : read
   - w : write
   - x : execute
   - (-) : tidak ada izin
       
## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari perintah `chmod`?
   **Jawaban:**  Perintah `chmod` berfungsi untuk mengubah izin akses (baca, tulis, eksekusi) pada berkas dan direktori.
2. Apa arti dari kode permission `rwxr-xr--`?
   **Jawaban:**  kode permission `rwxr-xr--` berarti owner memiliki izin akses baca(r), tulis(w), dan eksekusi(x). Sedangkan grup memiliki izin akses baca dan eksekusi, dan others memiliki izin akses hanya baca saja.
3. Jelaskan perbedaan antara chown dan chmod.
   **Jawaban:**  perintah `chown` berfungsi untuk mengubah kepemilikan sebuah berkas atau direktori, sedangkan perintah `chmod` berfungsi untuk mengubah izin aksesnya.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Memahami perintah linux dan fungsinya.
- Bagaimana cara Anda mengatasinya?  Mempelajarinya lewat berbagai sumber di internet.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
