# NIM/Nama: 19623099/Daniel Pedrosa Wu
# Tanggal: 5 Oktober 2023
# Deskripsi: Membuat piramida angka

# KAMUS
# P = int
# S = int
# Kelipatan = int
# Baris = int
# K = int

# ALGORITMA
# Input
P = int(input("Masukkan panjang piramida: "))
S = int(input("Masukkan selisih: "))

# Proses
Kelipatan = 0
Baris = 1
K = 0
if((P % 2) == 0):
    P = P - 1

if (P > 75):
    print("Invalid")   
else: 
    while (Kelipatan <= 75) and (K < ((P + 1) / 2)):
        for j in range(1, (P // 2) + 1 - Kelipatan):
            print("X", end = '')
        for j in range((P // 2), (P // 2) + 1 + 2 * Kelipatan):
            print(Baris, end = '')
        for j in range ((P // 2) + 1 + Kelipatan, P):
            print("X", end = '')
        print()
        Kelipatan = Kelipatan + 1
        if (Baris < 10):
            Baris = Baris + S
            if (Baris >= 10): 
                Baris = Baris % 10
        K = K + 1