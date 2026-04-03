# 🗂️ File Organizer Otomatis

Script Python yang secara otomatis merapikan file di folder berdasarkan jenisnya. Tersedia dalam versi Python script maupun `.exe` yang bisa langsung dijalankan tanpa instalasi Python.

## ✨ Fitur
- ✅ Rapiin file yang sudah ada sekaligus
- ✅ Pantau folder secara real-time (file baru langsung dirapiin)
- ✅ Catat semua aktivitas ke file `organizer.log`
- ✅ Otomatis handle nama file yang duplikat
- ✅ Tersedia versi `.exe` — tidak perlu install Python

## 📁 Kategori Folder

| Folder | Ekstensi |
|--------|----------|
| Images | .jpg .jpeg .png .gif .svg .webp .bmp .ico .tiff |
| Videos | .mp4 .mkv .avi .mov .wmv .flv .webm .m4v |
| Documents | .pdf .docx .doc .xlsx .pptx .txt .csv .odt |
| Music | .mp3 .wav .flac .aac .ogg .m4a .wma .opus |
| Archives | .zip .rar .tar .gz .7z .bz2 |
| Code | .py .js .html .css .json .ts .php .rb .go .md .sql |
| Installers | .exe .msi .dmg .pkg .deb .rpm |
| Fonts | .ttf .otf .woff .woff2 .eot |
| Others | semua ekstensi lainnya |

## 🚀 Cara Pakai

### Opsi 1 — Pakai `.exe` (Paling mudah, tidak perlu Python)

1. Download `FileOrganizer.exe` dari folder `dist/`
2. Dobel klik file `.exe`
3. Masukkan path folder yang ingin dirapikan
4. Tekan `Ctrl+C` untuk berhenti

### Opsi 2 — Pakai Python Script

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Jalankan script**
```bash
# Dengan argumen langsung
python organizer.py "C:/Users/Kamu/Downloads"

# Atau tanpa argumen (akan ditanya interaktif)
python organizer.py
```

## 🛠️ Build `.exe` Sendiri

```bash
pip install pyinstaller
pyinstaller --onefile --name "FileOrganizer" organizer.py
```

File `.exe` akan ada di folder `dist/`.

## 📂 Struktur Project

```
file-organizer/
├── organizer.py      # Script utama
├── config.py         # Konfigurasi kategori file
├── requirements.txt  # Daftar library
├── README.md         # Dokumentasi
└── .gitignore        # Filter file yang di-push
```

## 🧰 Tech Stack

- Python 3.8+
- [watchdog](https://pypi.org/project/watchdog/) — untuk monitoring folder real-time
- [PyInstaller](https://pyinstaller.org/) — untuk build `.exe`
