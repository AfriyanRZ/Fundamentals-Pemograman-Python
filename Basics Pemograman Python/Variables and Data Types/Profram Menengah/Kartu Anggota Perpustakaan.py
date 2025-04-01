# Program Pendaftaran Anggota Perpustakaan 

# Input dari Pengguna
nama = input("Masukan nama anda: ") # String
umur = int(input("Masukan umur anda: ")) # Integer
status = input("Apakah anda pelajar? (ya/tidak): ").strip().lower() # String (diubah ke huruf kecil)

# Menentukan kategori usia 
if umur < 12:
    kategori = "Anak-anak"
    biaya = 10000  # Harga dasar untuk anak-anak
elif 12 <= umur < 18:
    kategori = "Remaja"
    biaya = 20000 # Harga dasar untuk remaja 
elif 18 <= umur < 50:
    kategori = "Dewasa"
    biaya = 30000 # Harga dasar untuk dewasa
else:
    kategori = "Lansia"
    biaya = 15000 # Harga dasar untuk lansia

# Diskon jika pengguna adalah pelajar
if status == "ya":
    biaya *= 0.8 # Diskon 20%

# Menampilkan kartu anggota perpustakaan
print("\n===== KARTU ANGGOTA PERPUSTAKAAN =====")
print(f"Nama         : {nama}")
print(f"Usia         : {umur} tahun")
print(f"Kategori     : {kategori}")
print(f"Status       : {'Pelajar' if status == 'ya' else 'umum'}")
print(f"Biaya Daftar : Rp{biaya:.2f}")
print("========================================")