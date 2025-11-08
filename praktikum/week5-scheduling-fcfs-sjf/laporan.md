
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  

---

## Dasar Teori

1. Penjadwalan CPU menentukan proses mana yang mendapat giliran menggunakan CPU untuk memaksimalkan efisiensi sistem.
2. FCFS (First Come First Served): proses dijalankan sesuai urutan kedatangan, mudah diterapkan tapi dapat menyebabkan waktu tunggu lama.
3. SJF (Shortest Job First): memilih proses dengan waktu eksekusi terpendek, menghasilkan waktu tunggu rata-rata paling kecil, namun sulit diterapkan karena durasi CPU burst sulit diprediksi.


---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
| SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |




4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```
---

## Kode / Perintah
```
Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
Turnaround Time (TAT) = WT + Burst Time
```

---

## Hasil Eksekusi

![screnshots hasil](<screenshots/EXPERIMENT 1.png>)
![Screenshot hasil](<screenshots/EXPERIMENT 2.png>)

---

## Analisis
1. Eksperimen 1 - FCFS (First Come First Served)
 -Tabel proses:
  
![screnshots hasil](<screenshots/EXPERIMENT 1.png>)

- Gantt Chart:
   ```
     | P1 | P2 | P3 | P4 |
     0    7    16    24   28
     ```

2. Eksperimen 2 - SFJ (Shortest Job First)
  - Tabel proses:

   ![Screenshot hasil](<screenshots/EXPERIMENT 2.png>)

- Gantt Chart
  
```
     | P1 | P2 | P3 | P4 |
     0    7    11    19   28
```  
     
   -  Tabel perbandingan FCFS dan SJF

  | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
  |------------|------------------|----------------------|------------|-------------|
  |FCFS | 10,25 | 17,25 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
  | SJF | 7,75 | 14,75 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |


Shortest Job First(SFJ) menjadi lebih unggul dari FCFS karena memproses proses terpendek lebih dulu sehingga mengurangi waktu tunggu untuk proses yang lain. FCFS mencegah starvation pada proses karena setiap proses akan mendapatkan kesempatan untuk dijalankan, tidak seperti SJF yang akan menyebabkan proses panjang tertunda terus menerus saat ada banyak proses pendek berdatangan.
     
---

## Tugas

![skenario](<screenshots/tugas skenario 1& 2.png>)

SKENARIO 1

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 9,5 | 16 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
| SJF | 8,5 | 15 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

SKENARIO 2

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 14,5 | 23,25 | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
| SJF | 13 | 21,75 | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |


## Kesimpulan
- Algoritma SJF memiliki rata rata waiting time dan turnaround time yang lebih kecil, karena SJF memprioritaskan proses dengan burst time terpendek. Tapi hal ini juga bisa menyebabkan starvation pada proses panjang jika banyak proses pendek berdatangan.
- Algoritma FCSF akan menjalankan perintah yang datang lebih dahulu. Namun algoritma ini menyebabkan waktu tunggu yang lama pada proses di belakang jika proses yang di depan memiliki burst time yang lama.
- SJF lebih efisien karena menghasilkan rata-rata waiting time dan turnaround time lebih kecil daripada FCFS.

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?
   **Jawaban:**  FCSF akan menjalankan proses yang datang terlebih dahulu sedangkan SJF akan memprioritaskan proses terpendek terlebih dahulu.
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?
   **Jawaban:**  Karena SJF menjalankan proses terpendek terlebih dahulu sehingga proses selanjutnya tidak akan menunggu terlalu lama.
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?
   **Jawaban:**  SJF akan menyebabkan starvation pada proses panjang karena SJF selalu memprioritaskan proses terpendek walaupun datang belakangan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Memahami materi.
- Bagaimana cara Anda mengatasinya?  Mempelajarinya lewat internet dan berdiskusi.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
