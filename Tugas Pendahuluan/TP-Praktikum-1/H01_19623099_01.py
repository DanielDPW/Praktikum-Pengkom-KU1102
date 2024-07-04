# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   12 September 2023
# Deskripsi :   Program Menentukan Kelulusan

# KAMUS
# Nilai1    :   float
# Nilai2    :   float
# Nilai3    :   float
# Nilai4    :   float
# RataRata  :   float
# Hasil     :   string

# ALGORITMA
# Input
Nilai1 = float(input("Masukkan nilai ujian 1: "))
Nilai2 = float(input("Masukkan nilai ujian 2: "))
Nilai3 = float(input("Masukkan nilai ujian 3: "))
Nilai4 = float(input("Masukkan nilai ujian 4: "))

# Proses
RataRata = (Nilai1 + Nilai2 + Nilai3 + Nilai4) / 4

if(0 <= Nilai1 <= 100) and (0 <= Nilai2 <= 100) and (0 <= Nilai3 <= 100) and (0 <= Nilai4 <= 100): # Memeriksa apakah nilai yang diinput berada dalam range 0-100
    if(Nilai1 >= 50) and (Nilai2 >= 50) and (Nilai3 >= 50) and (Nilai4 >= 50) and (RataRata >= 70):
        Hasil = "lulus"
    else: # Syarat kelulusan tidak terpenuhi.
        Hasil = "tidak lulus"
else: # Nilai yang dinput tidak berada dalam range 0-100.
    Hasil = ""

# Output
if(Hasil != ""):
    print(f"Tuan Kil {Hasil} kelas Tuan Leo.")
else: # Nilai yang diinput tidak berada dalam range 0-100.
    print("Nilai yang Anda masukkan tidak valid.")