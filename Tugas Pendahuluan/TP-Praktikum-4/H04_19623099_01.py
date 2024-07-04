# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   26 Oktober 2023
# Deskripsi :   Jumlah maksimum submatriks 2 x 2 yang memiliki elemen ganjil

# KAMUS
# m, n, maks, value : int
# matriks : list of list of int

# Fungsi IsMax
def IsMax(x, y):
    # Mencari apakah nilai x lebih besar dari nilai maks sebelumnya

    # KAMUS LOKAL
    # x, y : int

    # ALGORITMA
    if x > y:
        y = x
    return y

# ALGORITMA
# Input
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
print("Masukkan elemen matriks:")
matriks = [list(map(int, input().split()[0:n])) for i in range(m)]

# Proses
maks = 0

for i in range(m - 1):
    for j in range(n - 1): 
        # Periksalah matriks 2x2 yang memiliki elemen ganjil.
        if matriks[i][j] % 2 == 1 or matriks[i + 1][j] % 2 == 1 or matriks[i][j + 1] % 2 == 1 or matriks[i + 1][j + 1] % 2 == 1:
            value = matriks[i][j] + matriks[i + 1][j] + matriks[i][j + 1] + matriks[i + 1][j + 1] # Jika ada, maka jumlahkan elemen matriks itu.
            maks = IsMax(value, maks) # Periksa apakah nilai matriks tersebut lebih besar dari nilai maks sebelumnya.

# Output
if (maks == 0):
    print("Tidak ada submatriks 2x2 yang memenuhi syarat.")
else: # maks != 0
    print(f"Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil adalah {maks}.")