
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946 
- **Kelas** : 1 IKRA
---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Menghitung waiting time dan turnaround time pada algoritma RR dan Priority.
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.
3. Membandingkan performa algoritma RR dan Priority.
4. Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.


---

## Dasar Teori
- Penjadwalan CPU adalah tugas memilih proses yang menunggu dari antrean siap
dan mengalokasikan CPU untuk proses tersebut. CPU dialokasikan ke
proses yang dipilih oleh operator.
- Penjadwalan round-robin (RR) mengalokasikan CPU ke setiap proses untuk waktu kuantum tertentu. Jika proses tersebut tidak melepaskan CPU sebelum kuantum waktunya habis, proses tersebut akan dihentikan sementara, dan proses lain akan dihentikan. 
- Priority Scheduling menetapkan prioritas untuk setiap proses, dan CPU dialokasikan ke proses dengan prioritas tertinggi. Proses dengan prioritas yang sama dapat dijadwalkan dalam urutan FCFS atau menggunakan RR sc.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
  WT[i] = waktu mulai eksekusi - Arrival[i]
  TAT[i] = WT[i] + Burst[i]
```

---

## Hasil Eksekusi & Analisis

1. Eksperimen 1 - Round Robin (RR)
   - Time quantum (q) = 3
   - Perhitungan Waiting Time dan Turnaround Time menggunakahn:
     ```
     TAT = Finish Time - Arrival
     WT =  TAT - Burst Time
     ```
   - Tabel hasil:
     ![rr q 3](<screenshots/rr_3.jpg>)

   - Gantt Chart:
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | P4 | P3 |
     0    3    6    9   12   14   17   20    22
     ```

   2. Eksperimen 2 - Priority Scheduling (Non-Preemptive)
      - Perhitungan Waiting Time dan Turnaround Time menggunakan:
        ```
        WT[i] = waktu mulai eksekusi - Arrival[i]
        TAT[i] = WT[i] + Burst[i]
        ```
      - Tabel hasil:
        ![priority](<screenshots/priority.jpg>)

      - Tabel perbandingan RR dan Priority:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | 8.5 | 14 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | 5.25 | 10.75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

   3. Eksperimen 3 - Analisis Variasi Time Quantum
      - _time quantum (q)_ = 2:
        ![rr dengan q = 2](<screenshots/rr_2.jpg>)
      - _time quantum (q)_ = 5:
        ![rr dengan q = 5](<screenshots/rr_5.jpg>)
---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?  
   **Jawaban:**  Round Robin menggunakan sistem waktu siklus (kuantum) yang sama untuk semua proses untuk keadilan, sementara Priority Scheduling menjadwalkan proses berdasarkan tingkat prioritas yang ditetapkan, di mana proses dengan prioritas lebih tinggi akan dijalankan terlebih dahulu.
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?   
   **Jawaban:**  
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
