# Program untuk menampilkan nama dan umur pengguna

# Meminta pengguna memasukan nama (tipe data string)
nama = input("Masukan nama Anda: ")

# Meminta pengguna memasukkan umur (tipe data integer, dikonversi dari string ke integer)
umur = int(input("Masukan umur Anda: ")) 

# Menampilkan hasil dengan menggunakan f-String
print(f"Halo, {nama}! Anda berusia {umur} tahun.")