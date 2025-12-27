
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
1. Penjadwalan CPU menentukan proses mana yang mendapat giliran menggunakan CPU untuk memaksimalkan efisiensi sistem.
2. FCFS (First Come First Served): proses dijalankan sesuai urutan kedatangan, mudah diterapkan tapi dapat menyebabkan waktu tunggu lama.
3. SJF (Shortest Job First): memilih proses dengan waktu eksekusi terpendek, menghasilkan waktu tunggu rata-rata paling kecil, namun sulit diterapkan karena durasi CPU burst sulit diprediksi.


---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```py
import csv
import os

# BACA DATASET CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "dataset.csv")

proses_list = []

with open(CSV_FILE, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # lewati header

    for row in reader:
        proses_list.append({
            "proses": row[0],
            "arrival": int(row[1]),
            "burst": int(row[2])
        })


# FCFS ALGORITHM

def fcfs(processes):
    time = 0
    result = []

    for p in sorted(processes, key=lambda x: x["arrival"]):
        if time < p["arrival"]:
            time = p["arrival"]

        start = time
        waiting = start - p["arrival"]
        time += p["burst"]
        turnaround = time - p["arrival"]

        result.append({
            **p,
            "waiting": waiting,
            "turnaround": turnaround
        })

    return result

# SJF NON-PREEMPTIVE
def sjf_non_preemptive(processes):
    time = 0
    completed = []
    ready_queue = processes.copy()

    while ready_queue:
        available = [p for p in ready_queue if p["arrival"] <= time]

        if not available:
            time += 1
            continue

        p = min(available, key=lambda x: x["burst"])
        ready_queue.remove(p)

        waiting = time - p["arrival"]
        time += p["burst"]
        turnaround = time - p["arrival"]

        completed.append({
            **p,
            "waiting": waiting,
            "turnaround": turnaround
        })

    return completed



# TAMPILKAN HASIL

def print_table(title, data):
    print(f"\n{title}")
    print("Proses  Arrival  Burst  Waiting  Turnaround")

    total_wt = 0
    total_tat = 0

    for p in data:
        total_wt += p["waiting"]
        total_tat += p["turnaround"]

        print(f"{p['proses']:6} {p['arrival']:7} {p['burst']:6} "
              f"{p['waiting']:8} {p['turnaround']:11}")

    n = len(data)
    print("Rata-rata Waiting Time   :", total_wt / n)
    print("Rata-rata Turnaround Time:", total_tat / n)



if __name__ == "__main__":
    fcfs_result = fcfs(proses_list)
    sjf_result = sjf_non_preemptive(proses_list)

    print_table("HASIL SIMULASI FCFS", fcfs_result)
    print_table("HASIL SIMULASI SJF NON-PREEMPTIVE", sjf_result)

```

---

## Hasil Eksekusi
Dataset yang digunakan:
   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 7 |
   | P2 | 1 | 9 |
   | P3 | 2 | 8 |
   | P4 | 3 | 4 |

Output program:

![Screenshot hasil](<screenshots/cpuschedule.png>)

---

## Analisis
- Alur Program

  Program diawali dengan membaca data dari file `dataset.csv`. File tersebut memiliki informasi seperti nama proses, arrival time, dan burst time nya. Program menggunakan data tersebut untuk menyimulasikan penjadwalan CPU yaitu First Come First Served(FCFS) yang akan mengurutkan proses berdasarkan _Arrival Time_ nya, lalu menghitung Waiting Time dan _Turnaround Time_ nya dan Shortest Job First(SJF), yang mengurutkan proses berdasarkan _Burst Time_. Lalu, program akan mengeluarkan output berupa tabel.

- Perbandingan dengan Perhitungan Manual

  [screenshot hasil](<../week5-scheduling-fcfs-sjf/screenshots/EXPERIMENT 1.png>)
  [screenshot hasil](<../week5-scheduling-fcfs-sjf/screenshots/EXPERIMENT 2.png>)

  Dapat dilihat bahwa hasil perhitungan keduanya memiliki hasil yang sama. Namun, simulasi menggunakan program python memiliki keunggulan dalam kecepatan dan ke akuratan perhitungannya. Hal ini membuat perhitungan menggunakan simulasi lebih dapat diandalakan daripada perhitungan secara manual.

- Kelebihan dan Keterbatasan Simulasi
  
  - Kelebihan: Simulasi lebih unggul dalam keakuratan dan kecepatan perhitungan, terutama untuk penggunaan dataset yang besar.
  - Keterbatasan: Sangat bergantung pada ketepatan dataset dan juga tidak memperhitungkan interupsi yang sering terjadi pada sistem operasi sebenarnya

 
 
---

## Kesimpulan
- Dari praktikum ini dapat disimpulkan bahwa penggunaan simulasi penjadwalan cpu memiliki banyak keunggulan dibandingkan menggunakan perhitungan manual. 

- Output yang dihasilkan menunjukan bahwa algoritma _Shortest Job First_ (SJF) memiliki rata-rata Waiting Time dan TUrnaround Time yang lebih rendah dibandingkan algoritma _First Come First Served_ (FCFS)

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
**Jawaban:** Simulasi diperlukan untuk menguji algortima scheduling karena dengan menyimulasikannya memungkinkan kita untuk membandingkan beberapa algoritma dan mengetahui performanya masing-masing,serta mengetahui kekurangan dan kelebihan banyak algoritma dalam berbagai situasi.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
**Jawaban:** Jika dataset yang dipakai besar, perbedaan yang paling utama terletak pada kecepatan perhitungannya, simulasi akan memberi hasil lebih cepat daripada penghitungan manual, dan juga perhitungan manual sangat rentan terhadap _human error_ sehingga membuat simulasi lebih dapat di percaya dan juga lebih efisien.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
**Jawaban:** Algoritma yang lebih mudah diimplemantasikan yaitu algoritma _first come first served_ karena algoritma ini mengeksekusi proses yang datang terlebih dahulu, tanpa mengurutkan proses seperti prioritas dan burst time terlebih dahulu. 
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
