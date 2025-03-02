import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    percobaan = 0

    print("\n===== PERMAINAN TEBAK ANGKA =====")
    print("Saya telah memilih angka antara 1 hingga 100. Coba tebak!")

    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukan tebakanmu: "))
            percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu rendah ! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Kamu berhasil menebak angka {angka_rahasia} dalam {percobaan} percobaan.")
        except ValueError:
            print("Masukan angka yang valid!")

# Menjalankan permainan
tebak_angka()