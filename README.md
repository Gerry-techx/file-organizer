# 🗂️ File Organizer Otomatis

Script Python yang secara otomatis merapikan file di folder berdasarkan jenisnya.

## Fitur
- ✅ Rapiin file yang sudah ada sekaligus
- ✅ Pantau folder secara real-time (file baru langsung dirapiin)
- ✅ Catat semua aktivitas ke file `organizer.log`
- ✅ Otomatis handle nama file yang duplikat

## Kategori Folder
| Folder | Ekstensi |
|--------|----------|
| Images | .jpg .png .gif .svg .webp |
| Videos | .mp4 .mkv .avi .mov |
| Documents | .pdf .docx .xlsx .txt .csv |
| Music | .mp3 .wav .flac .aac |
| Archives | .zip .rar .tar .gz |
| Code | .py .js .html .css .json |
| Others | semua ekstensi lainnya |

## Cara Pakai

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan script
```bash
# Dengan argumen langsung
python organizer.py "C:/Users/Kamu/Downloads"

# Atau tanpa argumen (akan ditanya interaktif)
python organizer.py
```

## Struktur Project
```
file-organizer/
├── organizer.py      # Script utama
├── config.py         # Konfigurasi kategori file
├── requirements.txt  # Daftar library
├── organizer.log     # Log aktivitas (auto-generated)
└── README.md
```
