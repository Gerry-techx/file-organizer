# config.py
# File ini ibarat "kamus" buat si organizer
# Di sini kita atur: ekstensi file apa masuk ke folder mana

FILE_CATEGORIES = {
    "Images": [                              # File gambar/foto
        ".jpg", ".jpeg", ".png",
        ".gif", ".svg", ".webp",
        ".bmp", ".ico", ".tiff"
    ],
    "Videos": [                              # File video
        ".mp4", ".mkv", ".avi",
        ".mov", ".wmv", ".flv",
        ".webm", ".m4v"
    ],
    "Documents": [                           # File dokumen
        ".pdf", ".docx", ".doc",
        ".xlsx", ".xls", ".pptx",
        ".ppt", ".txt", ".csv",
        ".odt", ".ods", ".odp"
    ],
    "Music": [                               # File audio/musik
        ".mp3", ".wav", ".flac",
        ".aac", ".ogg", ".m4a",
        ".wma", ".opus"
    ],
    "Archives": [                            # File terkompresi
        ".zip", ".rar", ".tar",
        ".gz", ".7z", ".bz2",
        ".xz", ".tar.gz"
    ],
    "Code": [                                # File kode program
        ".py", ".js", ".html",
        ".css", ".json", ".ts",
        ".java", ".cpp", ".c",
        ".jsx", ".tsx", ".php",
        ".rb", ".go", ".rs",
        ".md", ".yaml", ".yml",
        ".xml", ".sql", ".sh"
    ],
    "Installers": [                          # BARU! File installer aplikasi
        ".exe", ".msi", ".dmg",
        ".pkg", ".deb", ".rpm",
        ".appimage", ".run"
    ],
    "Fonts": [                               # BARU! File font/huruf
        ".ttf", ".otf", ".woff",
        ".woff2", ".eot"
    ],
    "Others": []                             # Kalau gak ada yang cocok → masuk sini
}


# Fungsi ini tugasnya: cari tahu, file ini masuk kategori apa?
def get_category(file_extension):
    for category, extensions in FILE_CATEGORIES.items():  # Loop satu-satu semua kategori
        if file_extension.lower() in extensions:           # Kalau ekstensinya cocok...
            return category                                # ...kembalikan nama kategorinya
    return "Others"                                        # Kalau gak ada yang cocok, masuk "Others"
