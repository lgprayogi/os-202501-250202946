
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946
- **Kelas** : 1 IKRA

---

## 1. Pendahuluan
Page replacement adalah suatu teknik komputer dalam mengeluarkan page dari RAM saat memori penuh untuk memberi ruang saat page baru dibutuhkan. Ada beberapa algoritma yang dapat melakukan teknik ini, yang pertama yaitu algoritma First In First Out (FIFO), yaitu algoritma yang akan mengeluarkan page berdasarkan waktu masuknya atau page yang paling awal masuk akan menjadi pertama yang keluar, lalu algoritma Least Recently Used (LRU),yang mengeluarkan page yang paling jarang digunakan.  Menurut Silberschatz, dkk (2018) algoritma paling simpel adalah algoritma First In First Out (FIFO) yang mengaitkan setiap halaman dengan waktu saat halaman tersebut dimasukkan ke memori. Ketika sebuah halaman harus diganti, halaman tertua yang dipilih. Tujuan dari simulasi ini adalah untuk mengetahui manakah diantara dua algoritma tersebut yang paling efisien dalam mengelola page replacement. 



---

## 2. Metode lingkungan uji, langkah eksperimen, parameter/dataset, cara pengukuran.
### 2.1. Lingkungan Uji
- Bahasa Pemrograman : Python
- Sistem Operasi     : Windows 10
### 2.2. Langkah Eksperimen
a. Menyiapkan dataset berupa reference string dan jumlah frame memori.
b. Mengimplementasikan algoritma FIFO untuk simulasi page replacement.
c. Mengimplementasikan algoritma LRU untuk simulasi page replacement.
d. Menjalankan simulasi untuk kedua algoritma dengan dataset yang sama.
e. Mencatat jumlah page fault untuk masing-masing algoritma.
### 2.3. Parameter/Dataset
- Reference String : 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
- Jumlah Frame Memori : 3 frame
### 2.4. Cara Pengukuran
- Jika page sudah ada di memori, akan terjadi page hit
- Jika page belum ada di memori, akan terjadi page fault
- Menghitung jumlah page fault yang terjadi selama simulasi untuk masing-masing algoritma.


---

## 3. Hasil
- Output hasil simulasi:
![output](<screenshots/page_replacement.png>)
---

## 4. Pembahasan
Dari simulasi diatas, didapatkan output bahwa algoritma LRU memiliki jumlah page hit yang lebih sedikit dibandingkan dengan algoritma FIFO. Hal ini menunjukan bahwa algoritma LRU lebih efisien dalam mengelola page replacement dibandingkan dengan algoritma FIFO. Algoritma LRU memilih page yang paling jarang digunakan untuk diganti saat memori penuh, sehingga mengurangi kemungkinan terjadinya page fault. Sedangkan algoritma FIFO hanya mengandalkan urutan masuknya page, sehingga ada kemungkinan page yang sering di pakai juga ikut terganti sehingga di saat ingin digunakan lagi, akan mengalami page fault. 

---

## 5. Kesimpulan
Dari simulasi diatas dapat disimpulkan bahwa:
- Algoritma LRU lebih efisien dibandingkan dengan algoritma FIFO dalam mengelola page replacement.
- Algoritma FIFO memiliki resiko mengeluarkan page yang sering digunakan, sehingga meningkatkan jumlah page fault.
- Algoritma LRU mengeluarkan page yang paling jarang digunakan, sehingga mengurangi jumlah page fault.
- Pemilihan algoritma page replacement yang tepat dapat mempengaruhi kinerja sistem komputer secara signifikan.

---

## 6. Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?
**Jawaban:** Karena format IMRAD memiliki struktur yang jelas, setiap bagian laporan memiliki isi yang spesifik, mulai dari latar belakang, metode pengujian, hingga kesimpulan. Sehingga memudahkan pembaca untuk memahami isi laporan
2. Apa perbedaan antara bagian **Hasil** dan **Pembahasan**?
**Jawaban:** Bagian hasil berisi output atau keluaran yang dihasilkan dari eksperimen yang di ujikan, sedangkan bagian pembahasan merupakan bagian yang membahas keseluruhan simulasi dengan detail.
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?
**Jawaban:** Sitasi dan daftar pustaka penting karena untuk mengetahui sumber materi yang di cantumkan di dalam laporan, dan untuk menghindari plagiarisme.

---

## 7. Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? Menyusun isi laporan dengan format IMRAD yang benar.
- Bagaimana cara Anda mengatasinya?  Mempelajari contoh laporan dengan format IMRAD dan mengikuti panduan yang diberikan.

---

## 8. Daftar Pustaka
Silberschatz, A., Galvin, P. B., dan Gagné, G. (2018). _Operating System Concepts_. Edisi ke-10. Hoboken: John Wiley & Sons.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
