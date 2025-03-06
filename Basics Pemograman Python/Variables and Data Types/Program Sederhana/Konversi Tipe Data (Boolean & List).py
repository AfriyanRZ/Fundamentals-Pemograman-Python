# Program untuk mengecek apakah pengguna suka kopi dan memberikan rekomendasi minuman

# Membuat daftar (list) minuman favorit
minuman_favorit = ["Kopi", "Teh", "Jus"]

# Meminta pengguna menjawab apakah mereka suka kopi
# Konversi jawaban ke huruf kecil dengan .lower() dan bandingkan dengan "ya" untuk mendapatkan nilai boolean (True/False)
suka_kopi = input("Apakah Anda suka kopi? (ya/tidak): ").lower() == "ya"

# Menentukan output berdasarkan jawaban pengguna
if suka_kopi:
    print(f"Anda menyukai {minuman_favorit[0]}.")  # Jika suka kopi, tampilkan "Kopi"
else:
    print(f"Anda lebih memilih minuman lain, seperti {minuman_favorit[1]} atau {minuman_favorit[2]}.")  
    # Jika tidak suka kopi, tampilkan alternatif dari list (Teh dan Jus)
