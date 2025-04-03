import datetime

class Karyawan:
    def __init__(self, id_karyawan, nama, posisi, gaji):
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.posisi = posisi
        self.gaji = gaji
        self.absensi = []

    def catat_absen(self, status):
        tanggal = datetime.date.today()
        self.absensi.append({"tanggal": tanggal, "status": status})
        print(f"Absensi tercatat: {self.nama} - {tanggal} - {status}")

    def tampilkan_absensi(self):
        print(f"\nRiwayat Absensi {self.nama}:")
        for data in self.absensi:
            print(f"{data['tanggal']} - {data['status']}")

    def __str__(self):
        return f"{self.id_karyawan} - {self.nama} ({self.posisi}) - Gaji: Rp{self.gaji:,}"

class Perusahaan:
    def __init__(self, nama):
        self.nama = nama
        self.karyawan = []

    def tambah_karyawan(self, id_karyawan, nama, posisi, gaji):
        self.karyawan.append(Karyawan(id_karyawan, nama, posisi, gaji))
        print(f"Karyawan {nama} berhasil ditambahkan.")

    def tampilkan_karyawan(self):
        if not self.karyawan:
            print("Tidak ada karyawan.")
            return
        print(f"\nDaftar Karyawan {self.nama}:")
        for karyawan in self.karyawan:
            print(karyawan)

    def catat_absensi(self, id_karyawan, status):
        for karyawan in self.karyawan:
            if karyawan.id_karyawan == id_karyawan:
                karyawan.catat_absensi(status)
                return
            print("Karyawan tidak ditemukan!")

    def total_penggajian(self):
        total = sum(karyawan.gaji for karyawan in self.karyawan)
        print(f"\nTotal penggajian perusahaan: Rp{total:,}")

def main():
    perusahaan = Perusahaan("TechCorp")
    while True:
        print("\nMenu Manajemen Perusahaan:")
        print("1. Tambah Karyawan")
        print("2. Tampilkan Karyawan")
        print("3. Catat Absensi")
        print("4. Tampilkan Absensi Karyawan")
        print("5. Total Penggajian")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            id_karyawan = input("Masukan ID Karyawan: ")
            nama = input("Masukan Nama: ")
            posisi = input("Masukan Posisi: ")
            gaji = int(input("Masukan Gaji: "))
            perusahaan.tambah_karyawan(id_karyawan, nama, posisi, gaji)
        elif pilihan == "2":
            perusahaan.tampilkan_karyawan()
        elif pilihan == "3":
            id_karyawan = input("Masukan ID Karyawan: ")
            status = input("Masukan status (Hadir/Sakit/Cuti): ")
            perusahaan.catat_absensi(id_karyawan, status)
        elif pilihan == "4":
            id_karyawan = input("Masukan ID Karyawan: ")
            for karyawan in perusahaan.karyawan:
                if karyawan.id_karyawan == id_karyawan:
                    karyawan.tampilkan_absensi()
                    break
            else:
                print("Karyawan tidak ditemukan!")
        elif pilihan == "5":
            perusahaan.total_penggajian()
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
