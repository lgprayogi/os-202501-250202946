
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
   
---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?   
   **Jawaban:**  
2. Apa perbedaan antara `kill` dan `killall`? 
   **Jawaban:**  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
