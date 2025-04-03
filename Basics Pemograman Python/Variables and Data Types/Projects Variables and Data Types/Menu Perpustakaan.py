import datetime

class Buku:
    def __init__(self, judul, penulis, tahun_terbit, jumlah):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.jumlah = jumlah

    def __str__(self):
        return f"{self.judul} oleh {self.penulis} ({self.tahun_terbit}) - {self.jumlah} teresdia"
    
class Perpustakaan:
    def __init__(self):
        self.koleksi = []
        self.peminjaman = {}

    def tambah_buku(self, judul, penulis, tahun_terbit, jumlah):
        for buku in self.koleksi:
            if buku.judul.lower() == judul.lower():
                buku.jumlah += jumlah
                print(f"Jumlah buku '{judul}' diperbarui menjadi {buku.jumlah}.")
                return
        self.koleksi.append(Buku(judul, penulis, tahun_terbit, jumlah))
        print(f"Buku '{judul}' berhasil ditambahkan!")

    def tampilkan_buku(self):
        if not self.koleksi:
            print("Perpustakaan kosong.")
            return
        for buku in self.koleksi:
            print(buku)

    def pinjam_buku(self, nama_peminjam, judul):
        for buku in self.koleksi:
            if buku.judul.lower() == judul.lower() and buku.jumlah > 0:
                buku.jumlah -= 1
                tanggal_pinjam = datetime.date.today()
                tanggal_kembali = tanggal_pinjam + datetime.timedelta(days=7)
                self.peminjaman[nama_peminjam] = {
                    "judul": judul,
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": tanggal_kembali
                }
                print(f"{nama_peminjam} meminjam '{judul}'. Kembalikan sebelum {tanggal_kembali}.")
                return
        print(f"Buku '{judul}' tidak tersedia atau habis.")
    
    def kembalikan_buku(self, nama_peminjam):
        if nama_peminjam in self.peminjaman:
            judul = self.peminjaman[nama_peminjam]["judul"]
            for buku in self.koleksi:
                if buku.judul.lower() == judul.lower():
                    buku.jumlah += 1
                    break
            del self.peminjaman[nama_peminjam]
            print(f"{nama_peminjam} telah mengembalikan '{judul}'.")
        else:
            print(f"{nama_peminjam} tidak memiliki buku yang sedang dipinjam.")

def main():
    perpustakaan = Perpustakaan()
    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah Buku")
        print("2. Tampilkan Koleksi Buku")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Keluar")
        pilihan = input("Pilih Menu (1-5): ")

        if pilihan == "1":
            judul = input("Masukan judul buku: ")
            penulis = input("Masukan nama penulis: ")
            tahun_terbit = input("Masukan jumlah buku: ")
            jumlah = int(input("Masukan jumlah buku: "))
            perpustakaan.tambah_buku(judul, penulis, tahun_terbit, jumlah)
        elif pilihan == "2":
            perpustakaan.tampilkan_buku()
        elif pilihan == "3":
            nama_peminjam = input("Masukan nama peminjam: ")
            judul = input("Masukan judul buku yang ingin dipinjam: ")
            perpustakaan.pinjam_buku(nama_peminjam, judul)
        elif pilihan == "4":
            nama_peminjam = input("Masukan nama peminjam yang mengembalikan buku: ")
            perpustakaan.kembalikan_buku(nama_peminjam)
        elif pilihan == "5":
            print("Terimakasih! Program Selesai.")
            break
        else: 
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
