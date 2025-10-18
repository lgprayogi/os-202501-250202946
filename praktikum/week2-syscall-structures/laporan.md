
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
2. Diagram alur system call


![diagram syscall](<screenshots/syscall-diagram.jpg>)



3. Analisis

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

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
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
