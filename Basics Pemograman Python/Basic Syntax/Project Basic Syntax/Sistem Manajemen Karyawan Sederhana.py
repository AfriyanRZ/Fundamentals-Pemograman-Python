# Program Sistem Manajemen Karyawan Sederhana

# List untuk menyimpan data karyawan (berisi dictionary)
employees = []

# Fungsi untuk menampilkan daftar karyawan
def show_employees():
    """Menampilkan daftar semua karyawan yang terdaftar."""
    if not employees:
        print("\nTidak ada karyawan yang terdaftar!\n")
    else:
        print("\n=== Daftar Karyawan ===")
        for emp in employees:
            print(f"ID: {emp['id']}, Nama: {emp['nama']}, Jabatan: {emp['jabatan']}")
        print("-" * 40)

# Fungsi untuk menambahkan karyawan
def add_employee():
    """Menambahkan data karyawan baru ke dalam list."""
    emp_id = input("Masukkan ID Karyawan: ")
    name = input("Masukkan Nama Karyawan: ")
    position = input("Masukkan Jabatan Karyawan: ")
    
    # Membuat dictionary untuk menyimpan data karyawan
    employee = {"id": emp_id, "nama": name, "jabatan": position}
    employees.append(employee)
    print(f"Karyawan '{name}' telah ditambahkan!\n")

# Fungsi untuk mencari karyawan berdasarkan ID
def find_employee():
    """Mencari karyawan berdasarkan ID yang dimasukkan pengguna."""
    emp_id = input("Masukkan ID Karyawan yang dicari: ")
    found = None
    
    for emp in employees:
        if emp["id"] == emp_id:
            found = emp
            break
    
    if found:
        print(f"\nKaryawan Ditemukan: ID: {found['id']}, Nama: {found['nama']}, Jabatan: {found['jabatan']}\n")
    else:
        print("\nKaryawan tidak ditemukan!\n")

# Fungsi untuk menghapus karyawan berdasarkan ID
def remove_employee():
    """Menghapus karyawan berdasarkan ID yang dimasukkan pengguna."""
    emp_id = input("Masukkan ID Karyawan yang ingin dihapus: ")
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print(f"Karyawan '{emp['nama']}' telah dihapus!\n")
            return
    print("\nKaryawan tidak ditemukan!\n")

# Fungsi utama untuk menjalankan program
def main():
    """Menampilkan menu utama dan menangani pilihan pengguna."""
    while True:
        print("=== Sistem Manajemen Karyawan ===")
        print("1. Lihat Daftar Karyawan")
        print("2. Tambah Karyawan")
        print("3. Cari Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1-5): ")
        
        if choice == "1":
            show_employees()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            find_employee()
        elif choice == "4":
            remove_employee()
        elif choice == "5":
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!\n")

# Menjalankan program
if __name__ == "__main__":
    main()
