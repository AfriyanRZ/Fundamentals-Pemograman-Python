def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_ke_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_ke_celsius(kelvin):
    return kelvin - 273.15

def konversi_suhu():
    print("\n===== KONVERSI SUHU =====")
    print("Pilih jenis konversi:")
    print("1. Celsius ke Fahrenheit")
    print("2. Celsius ke Kelvin")
    print("3. Fahrenheit ke Celsius")
    print("4. Kelvin ke Celsius")
    
    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    
    if pilihan in ('1', '2', '3', '4'):
        suhu = float(input("Masukkan suhu: "))
        
        if pilihan == '1':
            hasil = celsius_ke_fahrenheit(suhu)
            print(f"{suhu}°C = {hasil:.2f}°F")
        elif pilihan == '2':
            hasil = celsius_ke_kelvin(suhu)
            print(f"{suhu}°C = {hasil:.2f}K")
        elif pilihan == '3':
            hasil = fahrenheit_ke_celsius(suhu)
            print(f"{suhu}°F = {hasil:.2f}°C")
        elif pilihan == '4':
            hasil = kelvin_ke_celsius(suhu)
            print(f"{suhu}K = {hasil:.2f}°C")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
konversi_suhu()
