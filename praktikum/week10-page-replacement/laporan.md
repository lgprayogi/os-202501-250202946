
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946 
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.
---

## Dasar Teori
1. Page replacement adalah suatu teknik komputer dalam mengeluarkan page dari RAM saat memori penuh untuk memberi ruang saat page baru dibutuhkan.
2. Algoritma FIFO mengaitkan setiap halaman dengan waktu ketika halaman tersebut dimasukkan ke memori. Ketika sebuah halaman harus diganti, halaman yang datang lebih dahulu akan dipilih.
3. Algoritma LRU memperhatikan waktu penggunaan terakhir halaman tersebut. Ketika sebuah halaman harus diganti, LRU memilih halaman yang paling lama tidak digunakan.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```py
import os
from collections import deque


def fifo(reference, frame_count):
    frames = []
    queue = deque()
    page_fault = 0
    table = []

    for page in reference:
        # CEK HIT / FAULT (SEBELUM GANTI)
        if page in frames:
            status = "HIT"
        else:
            status = "FAULT"
            page_fault += 1

            if len(frames) < frame_count:
                frames.append(page)
                queue.append(page)
            else:
                # FIFO: buang yang paling lama masuk
                old = queue.popleft()
                idx = frames.index(old)
                frames[idx] = page
                queue.append(page)

        table.append((page, frames.copy(), status))

    return page_fault, table


def lru(reference, frame_count):
    frames = []
    last_used = {}
    page_fault = 0
    table = []

    for time, page in enumerate(reference):
        # CEK HIT / FAULT (SEBELUM GANTI)
        if page in frames:
            status = "HIT"
        else:
            status = "FAULT"
            page_fault += 1

            if len(frames) < frame_count:
                frames.append(page)
            else:
                # LRU: cari page paling lama tidak dipakai
                lru_page = min(frames, key=lambda p: last_used[p])
                frames[frames.index(lru_page)] = page

        last_used[page] = time
        table.append((page, frames.copy(), status))

    return page_fault, table


def print_table(title, table, frame_count):
    print(f"\n{title}")
    print("-" * 50)
    header = "Page\t" + "\t".join([f"F{i+1}" for i in range(frame_count)]) + "\tStatus"
    print(header)
    print("-" * 50)

    for page, frames, status in table:
        row = f"{page}\t"
        for i in range(frame_count):
            row += f"{frames[i] if i < len(frames) else '-'}\t"
        row += status
        print(row)


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "reference_string.txt")

    with open(file_path, "r") as file:
        reference = list(map(int, file.read().split(",")))

    frame_count = 3

    fifo_fault, fifo_table = fifo(reference, frame_count)
    lru_fault, lru_table = lru(reference, frame_count)

    print_table("FIFO Page Replacement", fifo_table, frame_count)
    print(f"\nTotal Page Fault FIFO: {fifo_fault}")

    print_table("LRU Page Replacement", lru_table, frame_count)
    print(f"\nTotal Page Fault LRU: {lru_fault}")


if __name__ == "__main__":
    main()


```

---

## Hasil Eksekusi
![screenshot hasi](<screenshots/page_replacement.png>)

---

## Analisis

- Tabel Perbandingan

    | Algoritma | Jumlah Page Fault | Keterangan |
    |:--|:--:|:--|
    | FIFO | 10 | Page fault lebih banyak |
    | LRU | 9 | Page fault lebih sedikit |

- Mengapa jumlah fault bisa berbeda?
  **Jawaban:** Karena algoritma FIFO akan mengganti page sesuai urutan kedatangannya, hal ini memiliki resiko yaitu page yang masih sering digunakan ikut terganti, sehingga jumlah fault akan bertambah, sedangkan algoritma LRU mengganti page yang paling jarang digunakan.

- Jelaskan algoritma mana yang lebih efisien!
  **Jawaban:** Algoritma LRU lebih efisien dibandingkan algoritma FIFO, hal ini terbukti dalam simulasi diatas yang menghasilkan output jumlah page fault LRU yang lebih sedikit dibandingkan FIFO.
  

---

## Kesimpulan

Dari praktikum ini dapat disimpulkan bahwa algortima FIFO mengganti page sesuai urutan kedatangan, sedangkan algoritma LRU mengganti page yang paling jarang digunakan. Hasil dari simulasi yaitu algoritma LRU (Least Recently Used) menghasilkan page fault yang lebih sedikit dibandingkan algoritma FIFO (First In First Out), karena itu dapat disimpulkan bahwa algoritma LRU lebih efisien dibandingkan algoritma FIFO.

---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?
**Jawaban:** Perbedaan utama FIFO dan LRU ada pada cara kedua algoritma tersebut mengganti _page_. Pada FIFO, _page_ dikeluarkan berdasarkan urutan kedatangan sedangkan algoritma LRU mengganti _page_ yang paling lama tidak digunakan.
2. Mengapa FIFO dapat menghasilkan *Belady’s Anomaly*?
**Jawaban:** FIFO dapat menghasilkan Belady’s Anomaly karena algoritma ini tidak mempertimbangkan waktu penggunaan page/halaman, sehingga penambahan frame dapat menyebabkan banyak halaman penting terganti dan meningkatkan jumlah page fault.
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
**Jawaban:** Karena LRU mengganti halaman yang paling jarang digunakan, sehingga saat frame berikutnya menggunakan halaman yang sering dipakai, page fault akan berkurang.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Memahami tentang _Belady's Anomaly_ dan cara membuat simulasi algoritma page replacement.
- Bagaimana cara Anda mengatasinya?  Mempelajarinya melalui berbagai sumber.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
