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
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("organizer.log"),
        logging.StreamHandler()
    ]
)


# ─── Fungsi Utama: Pindahin File ─────────────────────────────────
def organize_file(file_path):
    file_path = Path(file_path)

    if not file_path.is_file():
        return

    file_extension = file_path.suffix
    category = get_category(file_extension)

    destination_folder = file_path.parent / category
    destination_folder.mkdir(parents=True, exist_ok=True)
    destination = destination_folder / file_path.name

    if destination.exists():
        base = file_path.stem
        ext  = file_path.suffix
        counter = 1
        while destination.exists():
            destination = destination_folder / f"{base}_{counter}{ext}"
            counter += 1

    shutil.move(str(file_path), str(destination))
    logging.info(f"Dipindahkan: {file_path.name} → {category}/")


# ─── Class Event Handler ─────────────────────────────────────────
class FileHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        time.sleep(1)
        organize_file(event.src_path)


# ─── Fungsi untuk Rapiin File yang Sudah Ada ─────────────────────
def organize_existing_files(folder_path):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            organize_file(file)


# ─── Fungsi Utama: Jalankan Monitoring ───────────────────────────
def start_monitoring(folder_to_watch):
    folder_to_watch = Path(folder_to_watch)

    if not folder_to_watch.exists():
        print(f"❌ Folder tidak ditemukan: {folder_to_watch}")
        return

    print(f"🗂️  Merapikan file yang sudah ada di: {folder_to_watch}")
    organize_existing_files(folder_to_watch)

    print(f"👁️  Mulai memantau folder: {folder_to_watch}")
    print("   Tekan Ctrl+C untuk berhenti.\n")

    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(folder_to_watch), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        print("\n✅ Pemantauan dihentikan.")

    observer.join()


# ─── Entry Point ─────────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    print("=" * 50)
    print("   🗂️  FILE ORGANIZER OTOMATIS")
    print("=" * 50)

    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("\n📁 Masukkan path folder yang ingin dirapikan: ").strip()

    try:
        start_monitoring(folder)
    except Exception as e:
        print(f"\n❌ Terjadi error: {e}")

    input("\n🔚 Tekan Enter untuk keluar...")    # Baris baru! Tahan window supaya tidak nutup
