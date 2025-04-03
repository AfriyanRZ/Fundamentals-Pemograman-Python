class Inventory:
    def __init__(self):
        self.items = [] # List untuk menyimpan item dalam bentuk dictionary

    def tambah_item(self, nama: str, jumlah: int, harga: float):
        item = {
            "nama": nama,
            "jumlah": jumlah,
            "harga": harga
        }
        self.items.append(item)
        print(f"Item '{nama}' berhasil ditambahkan!")

    def tampilkan_inventory(self):
        if not self.items:
            print("Inventaris kosong.")
            return

        print("\nDaftar Inventaris:")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item['nama']} - jumlah: {item['jumlah']} - Harga: Rp{item['harga']:.2f}")

    def hapus_item(self, nama: str):
        for item in self.items:
            if item["nama"].lower() == nama.lower():
                self.items.remove(item)
                print(f"Item '{nama}' berhasil dihapus!")
                return
        print(f"Item '{nama}' tidak ditemukan!")

    def total_nilai_inventory(self):
        total = sum(item['jumlah'] * item['harga'] for item in self.items)
        print(f"\nTotal nilai inventaris: Rp{total:.2f}")


def main():
    inventory = Inventory()
    while True:
        print("\nMenu:")
        print("1. Tambah Item")
        print("2. Tampilkan Inventaris")
        print("3. Hapus Item")
        print("4. Total Nilai Inventaris")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            nama = input("Masukan nama item: ")
            jumlah = int(input("Masukan jumlah: "))
            harga = float(input("Masukan harga: "))
            inventory.tambah_item(nama, jumlah, harga)
        elif pilihan == "2":
            inventory.tampilkan_inventory()
        elif pilihan == "3":
            nama = input("Masukan nama item yang akan dihapus: ")
            inventory.hapus_item(nama)
        elif pilihan == "4":
            inventory.total_nilai_inventory()
        elif pilihan == "5":
            print("Terimakasih! Program Selesai.")
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()