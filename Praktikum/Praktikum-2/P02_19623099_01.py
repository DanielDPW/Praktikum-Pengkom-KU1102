# NIM/Nama: 19623099/Daniel Pedrosa Wu
# Tanggal: 5 Oktober 2023
# Deskripsi: Menentukan berapa kegiatan dalam gedung A dan B

# KAMUS
# N = int
# Kegiatan = int
# A = int
# B = int

# ALGORITMA
# Input
N = int(input("Masukkan nilai N: "))

# Proses
Kegiatan = 1
A = 0
B = 0

while (B < 3):
    P = int(input(f"Masukkan bilangan ke-{Kegiatan}: "))
    if (P < N) and (A < 5) and (B < 3):
        A = A + 1
    elif(P < N) and (A >= 5) and (B < 3):
        B = B + 1
    elif(P >= N)and (B < 3):
        B = B + 1
    Kegiatan = Kegiatan + 1

print(f"Terdapat {A} kegiatan di gedung A dan {B} kegiatan di gedung B.")