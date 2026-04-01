# config.py
# File ini ibarat "kamus" buat si organizer
# Di sini kita atur: ekstensi file apa masuk ke folder mana

FILE_CATEGORIES = {                          # Bikin dictionary (kamus) kategori file
    "Images": [                              # Kalau ekstensinya salah satu di bawah ini → masuk folder "Images"
        ".jpg", ".jpeg", ".png",
        ".gif", ".svg", ".webp", ".bmp"
    ],
    "Videos": [                              # Kalau video → masuk folder "Videos"
        ".mp4", ".mkv", ".avi",
        ".mov", ".wmv", ".flv"
    ],
    "Documents": [                           # Dokumen → masuk folder "Documents"
        ".pdf", ".docx", ".doc",
        ".xlsx", ".xls", ".pptx",
        ".txt", ".csv"
    ],
    "Music": [                               # Musik/audio → masuk folder "Music"
        ".mp3", ".wav", ".flac",
        ".aac", ".ogg", ".m4a"
    ],
    "Archives": [                            # File zip/rar dll → masuk folder "Archives"
        ".zip", ".rar", ".tar",
        ".gz", ".7z"
    ],
    "Code": [                                # File kode program → masuk folder "Code"
        ".py", ".js", ".html",
        ".css", ".json", ".ts",
        ".java", ".cpp", ".c"
    ],
    "Others": []                             # Kalau ekstensinya gak ada di atas → masuk "Others"
}

# Fungsi ini tugasnya: cari tahu, file ini masuk kategori apa?
def get_category(file_extension):
    for category, extensions in FILE_CATEGORIES.items():  # Loop satu-satu semua kategori
        if file_extension.lower() in extensions:           # Kalau ekstensinya cocok...
            return category                                # ...kembalikan nama kategorinya
    return "Others"                                        # Kalau gak ada yang cocok, masuk "Others"
