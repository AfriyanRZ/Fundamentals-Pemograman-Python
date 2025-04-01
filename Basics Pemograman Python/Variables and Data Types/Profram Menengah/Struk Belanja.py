# Program menghitung total belanja dengan berbagai tipe data

# Variabel dengan berbagai tipe data
nama_pembeli = input("Masukkan nama anda: ")     # String
nama_barang = input("Masukkan nama barang yang dibeli: ") # String
jumlah_barang = int(input("Masukan jumlah barang: ")) # Integer
harga_per_barang = float(input("Masukan harga per barang: ")) # Float
diskon_aktif = input("Apakah ada diskon? (ya/tidak): ").lower() == "ya" # Boolean

# Menghitung total harga sebelum diskon
total_harga = jumlah_barang * harga_per_barang

# Jika ada diskon, terapkan potongan 10%
if diskon_aktif:
    total_harga *= 0.9 # Mengurangi 10%

# Menampilkan hasil
print("\n========== STRUK BELANJA ==========")
print(f"Nama Pmbeli    : {nama_pembeli}")
print(f"Barang Dibeli  : {nama_barang}")
print(f"Jumlah Barang  : {jumlah_barang}")
print(f"Harga Satuan   : RP{harga_per_barang:.2f}")
print(f"Total Harga    : RP{total_harga:.2f}")
if diskon_aktif:
    print("✅ Diskon 10% telah diterapkan!")
print("======================================")