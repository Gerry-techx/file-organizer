# organizer.py
# Ini file utama! Di sinilah semua "keajaiban" terjadi.
# Script ini bakal pantau folder & otomatis rapiin file.

import os                          # Untuk urusan sistem file & folder
import shutil                      # Untuk mindahin / meng-copy file
import logging                     # Untuk nyetak log (catatan aktivitas)
import time                        # Untuk bikin jeda waktu
from pathlib import Path           # Cara modern Python untuk urus path file
from watchdog.observers import Observer          # "Mata-mata" yang pantau folder
from watchdog.events import FileSystemEventHandler  # Kelas untuk handle event file
from config import get_category    # Import fungsi dari config.py yang kita buat tadi


# ─── Setup Logging ───────────────────────────────────────────────
# Logging itu kayak "buku catatan" — semua aktivitas script dicatat di sini
logging.basicConfig(
    level=logging.INFO,                          # Catat semua info penting
    format="%(asctime)s - %(message)s",          # Format: [waktu] - [pesan]
    handlers=[
        logging.FileHandler("organizer.log"),    # Simpan catatan ke file organizer.log
        logging.StreamHandler()                  # Sekaligus tampilkan di terminal
    ]
)


# ─── Fungsi Utama: Pindahin File ─────────────────────────────────
def organize_file(file_path):
    """
    Fungsi ini tugasnya satu: ambil file, tentuin masuk folder mana, lalu pindahin.
    """
    file_path = Path(file_path)                  # Ubah string path jadi objek Path

    if not file_path.is_file():                  # Kalau ternyata bukan file (misal folder), skip aja
        return

    file_extension = file_path.suffix            # Ambil ekstensinya, misal: ".mp3", ".pdf"
    category = get_category(file_extension)      # Tanya ke config.py: "ini masuk kategori apa?"

    # Tentukan folder tujuan: folder induk si file + nama kategori
    # Contoh: /Downloads/Music
    destination_folder = file_path.parent / category

    # Kalau folder tujuan belum ada, buat dulu
    destination_folder.mkdir(parents=True, exist_ok=True)

    # Tentukan path lengkap tujuan file
    # Contoh: /Downloads/Music/lagu.mp3
    destination = destination_folder / file_path.name

    # Kalau ternyata di folder tujuan sudah ada file dengan nama sama...
    if destination.exists():
        # ...kita kasih tambahan angka di belakang nama filenya
        # Contoh: lagu.mp3 → lagu_1.mp3
        base = file_path.stem                    # Nama file tanpa ekstensi: "lagu"
        ext  = file_path.suffix                  # Ekstensinya: ".mp3"
        counter = 1
        while destination.exists():              # Terus nambah angka sampai namanya unik
            destination = destination_folder / f"{base}_{counter}{ext}"
            counter += 1

    shutil.move(str(file_path), str(destination))        # Pindahin filenya!
    logging.info(f"Dipindahkan: {file_path.name} → {category}/")  # Catat di log


# ─── Class Event Handler ─────────────────────────────────────────
# Class ini kayak "satpam" — dia bereaksi setiap kali ada file baru masuk
class FileHandler(FileSystemEventHandler):

    def on_created(self, event):
        """
        Fungsi ini otomatis dipanggil setiap kali ada file BARU muncul di folder.
        """
        if event.is_directory:                   # Kalau yang muncul folder, bukan file → abaikan
            return

        time.sleep(1)                            # Tunggu 1 detik dulu, biar file selesai ter-download/ter-copy
        organize_file(event.src_path)            # Baru deh panggil fungsi untuk pindahin


# ─── Fungsi untuk Rapiin File yang Sudah Ada ─────────────────────
def organize_existing_files(folder_path):
    """
    Fungsi ini untuk rapiin file-file yang SUDAH ADA di folder sebelum script dijalankan.
    """
    folder = Path(folder_path)                   # Ubah path jadi objek Path

    for file in folder.iterdir():                # Loop semua isi folder satu per satu
        if file.is_file():                       # Kalau isinya file (bukan subfolder)...
            organize_file(file)                  # ...pindahin!


# ─── Fungsi Utama: Jalankan Monitoring ───────────────────────────
def start_monitoring(folder_to_watch):
    """
    Fungsi ini yang nyalain "mode pantau" — script akan terus jalan di background
    dan bereaksi setiap kali ada file baru.
    """
    folder_to_watch = Path(folder_to_watch)

    # Cek dulu, foldernya beneran ada gak?
    if not folder_to_watch.exists():
        print(f"❌ Folder tidak ditemukan: {folder_to_watch}")
        return

    print(f"🗂️  Merapikan file yang sudah ada di: {folder_to_watch}")
    organize_existing_files(folder_to_watch)     # Rapiin file lama dulu

    print(f"👁️  Mulai memantau folder: {folder_to_watch}")
    print("   Tekan Ctrl+C untuk berhenti.\n")

    event_handler = FileHandler()                # Buat "satpam"-nya
    observer = Observer()                        # Buat "mata-mata"-nya (watchdog)
    observer.schedule(
        event_handler,                           # Pasang satpam ke mata-mata
        str(folder_to_watch),                    # Folder yang dipantau
        recursive=False                          # Jangan masuk ke subfolder
    )

    observer.start()                             # Mulai pantau!

    try:
        while True:                              # Terus jalan sampai di-stop manual
            time.sleep(5)                        # Cek setiap 5 detik
    except KeyboardInterrupt:                    # Kalau user pencet Ctrl+C...
        observer.stop()                          # ...hentikan pemantauan
        print("\n✅ Pemantauan dihentikan.")

    observer.join()                              # Tunggu semua proses selesai dengan bersih


# ─── Entry Point ─────────────────────────────────────────────────
# Bagian ini yang dijalankan pertama kali saat kamu ketik: python organizer.py
if __name__ == "__main__":
    import sys

    # Kalau user kasih path folder lewat terminal (misal: python organizer.py C:/Downloads)
    if len(sys.argv) > 1:
        folder = sys.argv[1]                     # Ambil argumen pertama sebagai path
    else:
        # Kalau tidak ada argumen, tanya ke user secara interaktif
        folder = input("📁 Masukkan path folder yang ingin dirapikan: ").strip()

    start_monitoring(folder)                     # Mulai jalankan semua!
