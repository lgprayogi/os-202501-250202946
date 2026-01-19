
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : Lintang Galih Prayogi
- **NIM**   : 250202946
- **Kelas** : 1 IKRA

---

## 1. Pendahuluan   

### 1.1. Latar Belakang
Dalam sistem operasi, memori utama (RAM) memiliki kapasitas yang terbatas, sementara seringkali program dan data yang dijalankan memerlukan lebih banyak ruang daripada yang tersedia. Untuk mengatasi hal ini, sistem operasi menggunakan memori virtual, yang memungkinkan sistem menyimpan sebagian data atau program penyimpanan sekunder seperti hard disk atau SSD secara sementara. Saat halaman penuh dan sistem perlu memuat data baru, maka sistem harus memutuskan data mana yang akan dganti dan yang akan tetap di memori. Proses ini disebut sebagai page replacement. Dalam page replacement, terdapat beberapa algoritma yang digunakan untuk menentukan halaman mana yang akan diganti, di antaranya sebagai berikut:

A. Algoritma First In First Out (FIFO)          
Algoritma yang paling sederhana adalah algoritma First In First Out (FIFO). Algoritma ini mengaitkan setiap halaman dengan waktu saat halaman tersebut dimasukkan ke memori. Ketika sebuah halaman harus diganti, halaman tertua yang dipilih. (Silberschatz et al., 2018)      
Algoritma ini menghitung berapa lama sebuah page menetap di memori. Saat memori penuh dan sistem ingin memuat page baru, algoritma ini akan memilih page yang memiliki waktu paling lama berapa di memori. 

B. Least Recently Used (LRU)            
Pendekatan yang mendekati algoritma optimal dapat dibuat dengan memperhatikan pola penggunaan halaman. Halaman yang sering digunakan dalam beberapa instruksi terakhir kemungkinan besar akan kembali digunakan dalam waktu dekat. Sebaliknya, halaman yang sudah lama tidak digunakan kemungkinan besar akan tetap tidak digunakan untuk waktu yang cukup lama. Berdasarkan pemikiran ini, sebuah algoritma yang dapat diterapkan muncul: saat terjadi page fault, halaman yang paling lama tidak digunakan akan diganti. Strategi ini dikenal dengan sebutan LRU (Least Recently Used) paging. (Tanenbaum & Bos, 2015)        
Algoritma LRU akan memilih page yang paling jarang digunakan untuk diganti saat memori penuh. Dengan cara ini, algoritma LRU berusaha mempertahankan halaman yang lebih sering diakses dalam memori, sehingga mengurangi kemungkinan terjadinya page fault.

### 1.2. Rumusan Masalah
Berdasarkan latar belakang di atas, rumusan masalah dalam laporan ini adalah:
1. Bagaimana cara kerja algoritma FIFO dan LRU dalam page replacement?
2. Algoritma mana yang lebih efisien dalam mengelola page replacement berdasarkan jumlah page fault yang terjadi?
3. Apa dampak dari pemilihan algoritma page replacement terhadap kinerja sistem komputer?
4. Bagaimana implementasi kedua algoritma tersebut dalam simulasi page replacement?

### 1.3. Tujuan
Tujuan dari laporan ini adalah:
1. Menjelaskan cara kerja algoritma FIFO dan LRU dalam page replacement.
2. Mengimplementasikan simulasi page replacement menggunakan kedua algoritma tersebut.
3. Membandingkan efisiensi kedua algoritma berdasarkan jumlah page fault yang terjadi selama simulasi.
4. Menganalisis dampak pemilihan algoritma page replacement terhadap kinerja sistem komputer.
5. Menyajikan hasil simulasi dalam laporan.



---

## 2. Metode
### 2.1. Lingkungan Uji
- Bahasa Pemrograman : Python
- Sistem Operasi     : Windows 10
- Alat Bantu         : Visual Studio Code
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
### 3.1 Output hasil simulasi:
![output](<screenshots/page_replacement.png>)

### 3.2 Tabel Hasil Simulasi

A. Algoritma FIFO
| Page | F1 | F2 | F3 | Status|
|------|----|----|----|-------|
|  7   |  7 | -  | -  |Fault  |
|  0   |  7 | 0  | -  |Fault  |
|  1   |  7 | 0  | 1  |Fault  |
|  2   |  2 | 0  | 1  |Fault  |
|  0   |  2 | 0  | 1  |Hit    |
|  3   |  2 | 3  | 1  |Fault  |
|  0   |  2 | 3  | 0  |Fault  |
|  4   |  4 | 3  | 0  |Fault  |
|  2   |  4 | 2  | 0  |Fault  |
|  3   |  4 | 2  | 3  |Fault  |
|  0   |  0 | 2  | 3  |Fault  |
|  3   |  0 | 2  | 3  |Hit    |       
|  2   |  0 | 2  | 3  |Hit    |

Jumlah Page Fault : 10


B. Algoritma LRU
| Page | F1 | F2 | F3 | Status|
|------|----|----|----|-------|
|  7   |  7 | -  | -  |Fault  |
|  0   |  7 | 0  | -  |Fault  |
|  1   |  7 | 0  | 1  |Fault  |
|  2   |  2 | 0  | 1  |Fault  |
|  0   |  2 | 0  | 1  |Hit    |
|  3   |  2 | 0  | 3  |Fault  |
|  0   |  2 | 0  | 3  |Hit    |
|  4   |  4 | 0  | 3  |Fault  |
|  2   |  4 | 0  | 2  |Fault  |
|  3   |  4 | 3  | 2  |Hit    |
|  0   |  0 | 3  | 2  |Fault  |
|  3   |  0 | 3  | 2  |Hit    |
|  2   |  0 | 3  | 2  |Hit    |

Jumlah Page Fault : 9

---

## 4. Pembahasan
### 4.1 Interpretasi Hasil
Berdasarkan hasil simulasi yang telah dilakukan, dapat dilihat bahwa algoritma LRU menghasilkan jumlah page fault yang lebih sedikit dibandingkan dengan algoritma FIFO. Berikut adalah tabel perbandingan jumlah page fault antara kedua algoritma:

| Algoritma | Cara kerja | Jumlah Page Fault | Keterangan          |
|-----------|---------|----------|---------------------|
| FIFO     |   Page yang pertama kali masuk akan dikeluarkan terlebih dahulu   |  10         | Page fault lebih banyak|
| LRU      |   Page yang paling jarang digunakan akan dikeluarkan terlebih dahulu   |  9          | Page fault lebih sedikit|

Berdasarkan tabel dan simulasi di atas, dapat disimpulkan bahwa algoritma LRU lebih efisien dalam mengelola page replacement dibandingkan dengan algoritma FIFO. Hal ini dikarenakan algoritma LRU mempertahankan halaman yang lebih sering diakses dalam memori, sehingga mengurangi kemungkinan terjadinya page fault.

### 4.2 Keterbatasan
Dalam simulasi ini, masih terdapat beberapa keterbatasan, antara lain:
1. Dataset yang digunakan kecil dan sederhana, sehingga hasil simulasi mungkin tidak sesuai dengan kondisi nyata pada sistem operasi yang asli.
2. Simulasi hanya dilakukan pada satu set reference string dan jumlah frame memori tertentu, sehingga hasilnya mungkin berbeda jika menggunakan dataset atau konfigurasi yang berbeda.
3. Implementasi algoritma dilakukan secara sederhana tanpa optimasi yang mungkin ada pada implementasi nyata

### 4.3 Perbandingan dengan Teori/Ekspektasi
Hasil simulasi yang diperoleh sesuai dengan teori yang ada tentang algoritma page replacement. Algoritma LRU dapat mengurangi jumlah page fault dibandingkan dengan algoritma FIFO, karena LRU mempertahankan halaman yang lebih sering diakses dalam memori. Hasil simulasi menunjukkan bahwa LRU memang menghasilkan jumlah page fault yang lebih sedikit dibandingkan dengan FIFO, sesuai dengan teori.

---

## 5. Kesimpulan
Berdasarkan hasil dari simulasi dan pembahasan yang telah dilakukan, dapat disimpulkan bahwa:
1. Algoritma FIFO bekerja dengan cara mengeluarkan halaman yang paling lama berada di memori terlebih dahulu, sedangkan algoritma LRU mengeluarkan halaman yang paling jarang digunakan.
2. Berdasarkan hasil simulasi, algoritma LRU lebih efisien dalam mengelola page replacement dibandingkan dengan algoritma FIFO, ditunjukkan dengan jumlah page fault yang lebih sedikit (9 page fault untuk LRU dibandingkan dengan 10 page fault untuk FIFO).
3. Pemilihan algoritma page replacement akan sangat memperngaruhi kinerja sistem komputer, terutama dalam hal jumlah page fault yang terjadi selama eksekusi program.
4. Implementasi kedua algoritma dalam simulasi menunjukkan perbedaan yang signifikan dalam jumlah page fault, yang mendukung teori yang ada tentang efisiensi algoritma page replacement.

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
Tanenbaum, A. S., dan Bos, H. (2015). _Modern Operating Systems_. Edisi ke-4. Harlow: Pearson Education Limited.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
