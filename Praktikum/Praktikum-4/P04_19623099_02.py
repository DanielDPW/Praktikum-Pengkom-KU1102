# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   2 November 2023
# Deskripsi :   Membuat matriks baru dari matriks sebelumnya

# KAMUS
# m, n : int
# matriks1, matriks2 : list of list of integers

# ALGORITMA
# Input
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))
matriks1 = [[0 for j in range(n)] for i in range(m)]
matriks2 = [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        matriks1[i][j] = int(input(f"Masukkan elemen matriks baris {i + 1} kolom {j + 1}: "))

# Proses
for i in range(m):
    for j in range(n):
        if i == 0 and j == 0:
            matriks2[i][j] = matriks1[i + 1][j] + matriks1[i][j + 1]
            # Cek dan jumlahkan yang di sekitar matriks.
        elif i == m - 1 and j == n - 1:
            matriks2[i][j] = matriks1[i - 1][j] + matriks1[i][j - 1]
            # Cek dan jumlahkan yang di sekitar matriks.
        elif i == 0 and  j == n - 1:
            matriks2[i][j] = matriks1[i + 1][j] + matriks1[i][j - 1]
            # Cek dan jumlahkan yang di sekitar matriks.
        elif i == m - 1 and j == 0:
            matriks2[i][j] = matriks1[i - 1][j] + matriks1[i][j + 1]
            # Cek dan jumlahkan yang di sekitar matriks.
        elif i == 0:
            matriks2[i][j] = matriks1[i + 1][j] + matriks1[i][j - 1] + matriks1[i][j + 1]
            # Cek dan jumlahkan yang di sekitar matriks.
        elif j == 0:
            matriks2[i][j] = matriks1[i][j + 1] + matriks1[i + 1][j] + matriks1[i - 1][j]
            # Cek dan jumlahkan yang di sekitar matriks.
        elif i == m - 1:
            matriks2[i][j] = matriks1[i - 1][j] + matriks1[i][j - 1] + matriks1[i][j + 1]
            # Cek dan jumlahkan yang di sekitar matriks.
        elif j == n - 1:
            matriks2[i][j] = matriks1[i][j - 1] + matriks1[i + 1][j] + matriks1[i - 1][j]
            # Cek dan jumlahkan yang di sekitar matriks.
        elif 0 < i < m - 1 and 0 < j < n - 1:
            matriks2[i][j] = matriks1[i][j + 1] + matriks1[i][j - 1] + matriks1[i + 1][j] + matriks1[i - 1][j]
            # Cek dan jumlahkan yang di sekitar matriks.

# Output
print("Matriks baru:")
for i in range(m):
    for j in range(n):
        print(f"{matriks2[i][j]} ", end = '')
    print()