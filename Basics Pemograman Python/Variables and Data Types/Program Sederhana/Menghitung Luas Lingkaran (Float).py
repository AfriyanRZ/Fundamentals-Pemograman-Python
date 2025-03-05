import math # Mengimpor modul math untuk menggunakan nilai x

# Meminta pengguna memasukan jari-jari lingkaran (tipe data float)
jari_jari = float(input("Masukan jari-jari lingkaran: "))

# Menghitung luas lingkaran dengan nama π * r^2
luas = math.pi * jari_jari ** 2

# Menghitung hasil perhitungan luas dengan pembulatan hingga 2 angka dibelakang koma
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas:2f}")