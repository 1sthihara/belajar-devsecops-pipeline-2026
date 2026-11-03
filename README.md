# Praktikum 12: Implementasi Pipeline CI/CD DevSecOps dengan GitHub Actions

Repositori ini berisi proyek praktik implementasi alur kerja DevSecOps dasar menggunakan GitHub Actions. Pipeline ini berfungsi sebagai gerbang keamanan (security gate) dan kualitas kode yang berjalan secara otomatis setiap kali ada perubahan kode (push) atau Pull Request ke branch utama.

## Arsitektur Pipeline CI/CD

Proyek ini menerapkan tiga tahapan utama (Jobs) dalam pipeline:

1. **Continuous Integration (CI) - SAST Scan:**
   - Alat: **Semgrep**
   - Fungsi: Melakukan pemindaian kode sumber secara statis (Static Application Security Testing) untuk mendeteksi celah keamanan berbahaya, seperti kerentanan SQL Injection pada aplikasi Flask.

2. **Continuous Integration (CI) - Code Quality Gate:**
   - Alat: **Pylint**
   - Fungsi: Memeriksa kualitas kode Python berdasarkan standar format PEP 8. Pipeline diatur agar hanya lolos jika skor Pylint mencapai ambang batas minimal (misal: >= 9.0).

3. **Continuous Deployment (CD) - Deploy to VM:**
   - Alat: **Docker** & **GitHub Self-Hosted Runner**
   - Fungsi: Membangun image Docker (`secure-flask-app`) dan menjalankan containernya di dalam Virtual Machine (Ubuntu Server lokal). Tahapan ini hanya akan dieksekusi jika kedua tahapan CI sebelumnya (Semgrep dan Pylint) berhasil dilewati.

## Struktur Repositori

- `.github/workflows/devsecops.yml`: File konfigurasi utama GitHub Actions yang mengatur seluruh job CI/CD.
- `app.py`: Source code utama aplikasi web (Flask).
- `Dockerfile`: Instruksi pengemasan aplikasi Python ke dalam lingkungan Docker.
- `requirements.txt`: Daftar dependensi modul Python yang dibutuhkan aplikasi.
- `templates/index.html`: File antarmuka web interaktif untuk sistem login.

## Mekanisme Branch Protection

Repositori ini dilindungi oleh **Branch Protection Rules** yang memastikan:
- Penghapusan branch utama dicegah secara otomatis (Restrict deletions).
- Setiap perubahan harus melalui proses *Pull Request* dan *Merge*.
- Penyatuan kode (*Merge*) diblokir (Require status checks to pass) apabila job Semgrep SAST atau Pylint Code Quality gagal atau menemukan error.

---
