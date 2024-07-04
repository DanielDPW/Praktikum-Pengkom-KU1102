# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   2 November 2023
# Deskripsi :   Menilai tugas praktikum

# KAMUS
# a, b, c : float
# soal1, soal2, soal3, nilai : int

# Fungsi cekvalid
    # Mencari apakah bobot nilai yang diinput valid

    # KAMUS LOKAL
    # x, y, z : float
    # valid : bool

    # ALGORITMA
def cekvalid(x, y, z):
    if 0 <= x <= 1 and 0 <= y <= 1 and 0 <= z <= 1 and x + y + z == 1: # cek apakah berada dalam rentang 0-1 dan jumlah total == 1
        valid = True
    else:
        valid = False
    return valid

# Fungsi hitung
    # Menghitung nilai akhir

    # KAMUS LOKAL
    # a, b, c, nilai : float
    # x, y, z : int

    # ALGORITMA
def hitung(a, b, c, x, y, z):
    if cekvalid(a, b, c):
        nilai = a * x + b * y + c * z
    return nilai

# ALGORITMA
# Input
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
soal1 = int(input("Masukkan nilai soal 1: "))
soal2 = int(input("Masukkan nilai soal 2: "))
soal3 = int(input("Masukkan nilai soal 3: "))

# Proses
nilai = 0

if not cekvalid(a, b, c):
    print("bobot tidak valid")
else:
    print(f"Nilai tugas praktikum adalah {hitung(a, b, c, soal1, soal2, soal3)}")