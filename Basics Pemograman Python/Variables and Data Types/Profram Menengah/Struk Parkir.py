# Program Manajemen Parkir

# Daftar tarif per jam berdasarkan jenis kendaran
tarif = {
    "motor": 2000, # Motor: Rp2000 per jam
    "mobil": 5000, # Mobil: Rp5000 per jam
    "truk": 8000   # Truk: Rp8000 per jam
}

# Input dari pengguna 
nama = input("Masukan nama anda: ") # String
jenis_kendaran = input("Jenis kendaran (motor/mobil/truk): ").strip().lower() # String
durasi = int(input("Lama parkir (dalam jam): ")) # Integer
is_member = input("Apakah anda member VIP? (ya/tidak): ").strip().lower() == "ya" # Boolean

# Validasi jenis kendaraan
if jenis_kendaran not in tarif:
    print("Jenis kendaraan tidak valid! Silahkan coba lagi.")
else:
    # Hitung biaya parkir
    biaya_parkir = durasi * tarif[jenis_kendaran]

    # Diskon 15% untuk member VIP
    if is_member:
        biaya_parkir *= 0.85

    # Tambahan biaya jika parkir lebih dari 12 jam
    if durasi > 12:
        biaya_parkir += 10000 # Denda tambahkan Rp10.000

    # Menampilkan struk parkir
    print("\n========== STRUK PARKIR ==========")
    print(f"Nama            : {nama}")
    print(f"Jenis Kendaraan : {jenis_kendaran.capitalize()}")
    print(f"Lama Parkir     : {durasi} jam")
    print(f"Status Member   : {'VIP' if is_member else 'reguler'}")
    print(f"Total Biaya     : Rp{biaya_parkir:.2f}")
    print("====================================")