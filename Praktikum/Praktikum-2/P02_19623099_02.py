# NIM/Nama: 19623099/Daniel Pedrosa Wu
# Tanggal: 5 Oktober 2023
# Deskripsi: Menentukan kelipatan angka

# KAMUS
# Baris = int
# Kelipatan = int
# Terlipat = boolean

# ALGORITMA
x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))

Baris = 1
Kelipatan = 1
Terlipat = False

if((y * Kelipatan) == 1):
    Kelipatan = Kelipatan + 1
    
for i in range(1, x + 1):
    print(f"{Baris} ", end ='')
    if (Terlipat == False):
        Baris = Baris + 1
        if ((Baris) == (y * Kelipatan)):
            Terlipat = True
            Kelipatan = Kelipatan + 1
    elif (Terlipat == True):
        Baris = Baris - 1
    if (Baris == 1):
        Terlipat = False