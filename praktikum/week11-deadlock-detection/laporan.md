
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
- Proses dikatakan mengalami deadlock saat dua atau lebih proses menunggu tanpa batas untuk suatu kejadian yang hanya dapat disebabkan oleh salah satu dari proses yang menunggu. 
- Ada empat syarat yang diperlukan agar deadlock terjadi: (1) mutual exclusion, (2) hold and wait, (3) no preemption, dan (4) circular wait.
- Deadlock dapat dicegah dengan memastikan salah satu dari empat kondisi tersebut tidak dapat terjadi.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
Potongan kode atau perintah utama:
```py
import os
import csv
from collections import defaultdict

# Baca dataset
processes = []
allocation = {}
request = {}

with open("d:/gitos/os-202501-250202946/praktikum/week11-deadlock-detection/code/dataset_deadlock.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row["Proses"]
        processes.append(p)
        allocation[p] = row["Allocation"]
        request[p] = row["Request"]
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](<screenshots/hasil_deteksi.png>)

---

## Analisis
- Tabel Proses  

   | Proses | Resource yang dipegang | Resource yang diminta |
   |:----:|:----:|:-----:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |


- Deadlock terjadi karena proses ini memenuhi 4 syarat terjadinya deadlock yaitu:
   - Mutual Exclusion : Hanya satu proses yang dapat mengakses sumber daya tertentu pada satu waktu
   - Hold and Wait : Terjadi ketika proses memiliki sumber daya dan menunggu sumber daya lain yang dimiliki oleh proses lain
   - No-preemption : Sumber daya yang dipegang proses tidak bisa di ambil paksa oleh proses lain
   - Circular wait : Kondisi di mana terjadi rantai proses yang saling bergantung untuk mendapatkan sumber daya

- Penjelasan : Satu resources hanya bisa di akses oleh satu proses pada satu waktu. Proses 1 memegang R1 dan meminta R2, namun R2 sedang dipegang oleh proses 2 yang sedang meminta R3 ke proses 3 yang juga sedang meminta R1 ke proses 1. Tidak ada proses yang dapat mengambil paksa sumber daya yang sedang dipegang proses lain, sehingga menyebabkan semua proses saling tunggu. Semua ini memenuhi 4 hal yang menyebabkan terjadinya deadlock

---

## Kesimpulan
- Deadlock terjadi saat dua atau lebih proses saling menunggu untuk suatu kejadian yang hanya dapat disebabkan oleh salah satu dari proses yang menunggu.
- Deadlock dapat dihindari dengan menghilangkan salah satu dari 4 kondisi yang menyebabkan deadlock
- Kesimpulan dari simulasi tersebut menunjukan bahwa data proses yang di sediakan menghasilkan output yaitu proses tersebut mengalami deadlock karena memenuhi 4 syarat tersebut.

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?  
 **Jawaban:**
     Perbedaan ketiganya adalah pada kapan itu terjadi:
     - Deadlock prevention mencegah deadlock terjadi sejak awal, misalnya membuat resource preemption (bisa di ambil paksa) atau melarang hold & wait
     - Deadlock avoidance menghindari deadlock terjadi saat proses sedang berjalan, hanya memberikan resource saat sistem dalam keadaan aman (*safe state*) misalnya menggunakan algoritma Banker
     - Deadlock detection tidak mengambil langkah awal untuk mencegah deadlock tetapi membiarkannya terjadi lalu menanganinya.
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
 **Jawaban:** Deteksi deadlock tetap diperlukan dalam sistem operasi karena masih banyak sistem yang belum bisa menerapkan deadlock prevention dan avoidance dengan efisien, dan juga untuk mengatasi deadlock jika keduanya terjadi kesalahan.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
 **Jawaban:**
   - Kelebihan:
     - Pemanfaatan resource lebih efisien karena tidak ada pembatasan ketat.
     - Implementasi relatif lebih sederhana dibandingkan deadlock avoidance.
     - Cocok untuk sistem besar dengan banyak proses dan resource.
   - Kekurangan:
     - Deadlock tetap bisa terjadi.
     - Proses pemulihan (recovery) dapat menyebabkan kehilangan data atau menghentikan proses penting.
     - Deteksi deadlock membutuhkan overhead komputasi untuk pemeriksaan secara berkala.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Menuliskan dan memahami simulasi deadlock detection
- Bagaimana cara Anda mengatasinya?  Mempelajarinya dari berbagai sumber di internet

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
