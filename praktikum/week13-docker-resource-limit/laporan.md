
# Laporan Praktikum Minggu 13
Topik: Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Lintang Galih Prayogi  
- **NIM**   : 250202946
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.
---

## Dasar Teori
- Docker menyediakan mekanisme untuk membatasi penggunaan CPU dan memori pada container agar aplikasi tidak menggunakan sumber daya sistem secara berlebihan. Pembatasan resource ini membantu menjaga kestabilan sistem ketika beberapa container dijalankan secara bersamaan.
- Virtualisasi memungkinkan pemanfaatan sumber daya sistem secara efisien dengan menjalankan beberapa lingkungan dalam satu mesin fisik. Manajemen resource diperlukan agar penggunaan CPU dan memori dapat dibagi secara terkontrol sehingga sistem tetap stabil.
- Sistem operasi memiliki mekanisme untuk mengatur dan membatasi penggunaan sumber daya oleh proses yang berjalan. Melalui pengelolaan resource, sistem dapat memastikan bahwa setiap proses berjalan dalam batas tertentu dan tidak mengganggu proses lain.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
Potongan kode atau perintah utama:
```bash
docker build -t week13-resource-limit .
docker run --rm week13-resource-limit
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit

```

---

## Hasil Eksekusi & Analisis
1. Hasil eksekusi tanpa limit
![hasil eksekusi tanpa limit](<screenshots/hasil_tanpaLimit.png>)

   - Saat program dijalanakan tanpa adanya pembatasan sumber daya, program akan terus berjalan tanpa hambatan dan terus melakukan peningkatan penggunaan memori.
   - Penggunaan memori meningkat secara bertahap tanpa adanya batasan, sehingga aplikasi tidak berhenti selama sumber daya sistem masih tersedia.

2. Hasil eksekusi dengan limit
![hasil eksekusi dengan limit](<screenshots/hasil_limit.png>)

   - Saat program dijalankan dengan pembatasan sumber daya, program tetap berjalan dengan normal pada awal eksekusi.
   - Namun, ketika penggunaan memori mencapai batas yang telah ditentukan, program berhenti dan tidak dapat melanjutkan proses eksekusi.
---

## Kesimpulan
- Hasil praktikum menunjukan bahwa pembatasan resource berpengaruh terhadap cara aplikasi dijalankan di dalam container.
- Docker memungkinkan aplikasi dijalankan secara terisolasi sehingga lebih mudah mengatur dan menguji penggunaan sumber daya sistem.
- Pembatasan CPU dan memori memengaruhi kinerja aplikasi,aplikasi dapat berjalan lebih lambat atau berhenti saat melebihi limit yang ditentukan.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?
**Jawaban:** Container perlu dibatasi CPU dan memori agar container tidak dapat mengambil seluruh resource host, mencegah out of memory yang dapat membunuh proses lain bahkan proses yang penting dan beresiko mematikan seluruh sistem jika proses yang salah terbunuh.
2. Apa perbedaan VM dan container dalam konteks isolasi resource?
**Jawaban:** 
   - Virtual Machine (VM) melakukan isolasi resource dengan menjalankan sistem operasi sendiri, sehingga penggunaan CPU dan memori benar-benar terpisah antar VM. Namun juga membutuhkan resource yang lebih besar.
   - Container melakukan isolasi dengan berbagi sistem operasi host, sehingga lebih ringan. Pembatasan CPU dan memori pada container bertujuan agar setiap aplikasi tetap terisolasi dan tidak saling mengganggu meskipun berjalan pada sistem yang sama.
3. Apa dampak limit memori terhadap aplikasi yang boros memori?
**Jawaban:** Aplikasi yang boros memori akan menjadi lambat, tidak dapat menyelesaikan suatu proses atau bahkan berhenti total jika melebihi limit memori yang di tetapkan.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
