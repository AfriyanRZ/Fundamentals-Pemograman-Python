# Program Manajemen Daftar Tugas (To-Do List)

# List untuk menyimpan tugas
tasks = []  # Variabel global untuk menyimpan daftar tugas

# Fungsi untuk menampilkan daftar tugas
def show_tasks():
    """Menampilkan daftar tugas yang tersimpan dalam list."""
    if not tasks:  # Mengecek apakah daftar tugas kosong
        print("\nDaftar tugas kosong!\n")
    else:
        print("\nDaftar Tugas:")
        for idx, task in enumerate(tasks, start=1):  # Loop untuk menampilkan setiap tugas dengan nomor
            print(f"{idx}. {task}")
    print("-" * 30)  # Garis pemisah untuk tampilan lebih rapi

# Fungsi untuk menambahkan tugas ke dalam daftar
def add_task():
    """Meminta input dari pengguna untuk menambahkan tugas baru."""
    task = input("Masukkan tugas baru: ")  # Input dari pengguna
    tasks.append(task)  # Menambahkan tugas ke dalam list
    print(f"Tugas '{task}' telah ditambahkan!\n")  # Konfirmasi kepada pengguna

# Fungsi untuk menghapus tugas berdasarkan nomor yang dimasukkan pengguna
def remove_task():
    """Menghapus tugas yang dipilih oleh pengguna dari daftar."""
    show_tasks()  # Menampilkan daftar tugas sebelum memilih yang akan dihapus
    try:
        idx = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1  # Konversi input ke integer
        if 0 <= idx < len(tasks):  # Memastikan nomor yang dimasukkan valid
            removed_task = tasks.pop(idx)  # Menghapus tugas dari list
            print(f"Tugas '{removed_task}' telah dihapus!\n")  # Konfirmasi penghapusan
        else:
            print("Nomor tugas tidak valid!\n")  # Pesan error jika nomor tidak ada di daftar
    except ValueError:  # Menangani error jika input bukan angka
        print("Masukkan angka yang valid!\n")

# Fungsi utama untuk menjalankan program
def main():
    """Menampilkan menu utama dan menangani pilihan pengguna."""
    while True:
        # Menampilkan menu utama
        print("=== Aplikasi To-Do List ===")
        print("1. Lihat Daftar Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        choice = input("Pilih opsi (1-4): ")  # Menerima input dari pengguna
        
        # Menggunakan percabangan untuk menjalankan fungsi sesuai pilihan pengguna
        if choice == "1":
            show_tasks()  # Menampilkan daftar tugas
        elif choice == "2":
            add_task()  # Menambahkan tugas
        elif choice == "3":
            remove_task()  # Menghapus tugas
        elif choice == "4":
            print("Terima kasih telah menggunakan aplikasi ini!")  # Keluar dari program
            break  # Menghentikan loop
        else:
            print("Pilihan tidak valid, coba lagi!\n")  # Menampilkan pesan error jika input tidak valid

# Menjalankan program hanya jika file ini dijalankan langsung
if __name__ == "__main__":
    main()  # Memanggil fungsi utama
