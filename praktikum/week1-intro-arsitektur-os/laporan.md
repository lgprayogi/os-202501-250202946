
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
4. 
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
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

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
  **Jawaban:** Cara mengoperasikan github
- Bagaimana cara Anda mengatasinya?
  **Jawaban:** Mencari tutorial di internet dan berdiskusi dengan orang lain.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
