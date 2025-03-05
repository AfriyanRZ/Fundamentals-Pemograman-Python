# Program Sistem Manajemen Perpustakaan Sederhana

# List untuk menyimpan data buku (setiap buku direpresentasikan sebagai dictionary)
library = []

# Fungsi untuk menampilkan semua buku dalam perpustakaan
def show_books():
    """Menampilkan daftar semua buku yang tersedia dalam perpustakaan."""
    if not library:
        print("\nPerpustakaan kosong! Tidak ada buku yang tersedia.\n")
    else: 
        print("\n=== Daftar Buku di Perpustakaan ===")
        for book in library:
            print(f"ID: {book['id']}, Judul: {book['title']}, Penulis: {book['author']}")
        print("-" * 40)

# Fungsi untuk menambahkan buku ke perpustakaan 
def add_book():
    """Menambahkan buku baru ke dalam perpustakaan."""
    book_id = input("Masukan ID Buku: ")
    title = input("Masukan Judul Buku: ")
    author = input("Masukan Nama Penulis: ")

    # Mmbuat dictionary untuk menyimpan data buku
    book = {"id": book_id, "title": title, "author": author}
    library.append(book) # Menambahkan buku ke dalam list library
    print(f"\nBuku '{title}' telah ditambahkan ke perpustakaan!\n")

# Fungsi untuk mencari buku berdasarkan judul
def find_book():
    """Mencari buku berdasarkan judul buku yang dimasukan pengguna."""
    search_title = input("Masukan judul buku yang dicari: ").lower() # Konversi ke huruf kecil untuk pencarian lebih fleksibel
    found_books = [book for book in library if book["title"].lower() == search_title] # Mencari buku dengan judul yang cocok

    if found_books:
        print("\n=== Buku Ditemukan ===")
        for book in found_books:
            print(f"ID: {book['id']}, Judul: {book['title']}, Penulis: {book['author']}")
    else: 
        print("\nBuku tidak ditemukan!\n")

# Fungsi untuk menghapus buku berdasarkan ID
def remove_book():
    """Menghapus buku dari perpustakaan berdasarkan ID yang dimasukan pengguna."""
    book_id = input("Masukan ID buku yang ingin dihapus: ")

    for book in library:
        if book["id"] == book_id:
            library.remove(book) # Menghapus buku dari list library
            print(f"\n Buku '{book['title']}' telah dihapus dari perpustakaan!\n")
            return # Keluar dari fungsi setelah buku dihapus
    
    print("\nBuku dengan ID tersebut tidak ditemukan!\n")

# Fungsi utama untuk menjalankan menu program
def main():
    """Menampilkan menu utama dan menangani pilihan pengguna."""
    while True:
        print("=== Sistem Manajemen Perpustakaan ===")
        print("1. Lihat Daftar Buku")
        print("2. Tambah Buku")
        print("3. Cari Buku")
        print("4. Hapus Buku")
        print("5. Keluar")

        choice = input("Pilih opsi (1-5): ")

        if choice == "1":
            show_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            find_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("\nTerima kasih telah menggunakan sistem perpustakaan!\n")
            break # Keluar dari loop dan menghentikan program
        else: 
            print("\nPilihan tidak valid, coba lagi!\n")

# Memastikan program hanya berjalan jika dijalankan sebgagai skrip utama
if __name__ == "__main__":
    main()

