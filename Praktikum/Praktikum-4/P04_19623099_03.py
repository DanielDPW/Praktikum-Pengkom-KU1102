# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   2 November 2023
# Deskripsi :   Keamanan raja dari serangan kuda

# KAMUS
# m : int
# papan : list of list of strings.

# ALGORITMA
# Input
m = int(input("Masukkan nilai m: "))
papan = [["." for j in range(m)] for i in range(m)]
for i in range(m):
    for j in range(m):
        papan[i][j] = str(input(f"Masukkan elemen matriks ke- {i + 1} {j + 1}: "))

# Proses
safe = True
for i in range(m):
    for j in range(m):
        if papan[i][j] == "K": # Cek apakah kuda sudah di sana dan carilah pergerakannya bisa ke mana saja. Dalam catur, dalam satu instansi kuda memiliki 8 pilihan pergerakan.
            if i + 1 < m and j + 2 < m:
                if papan[i + 1][j + 2] == "R":
                    safe = False
            if i - 1 >= 0 and j + 2 < m:
                if papan[i - 1][j + 2] == "R":
                    safe = False
            if i + 1 < m and j - 2 >= 0:
                if papan[i + 1][j - 2] == "R":
                    safe = False
            if i - 1 >= 0 and j - 2 >= 0:
                if papan[i - 1][j - 2] == "R":
                    safe = False
            if i + 2 < m and j + 1 < m:
                if papan[i + 2][j + 1] == "R":
                    safe = False
            if i - 2 >= 0 and j + 1 < m:
                if papan[i - 2][j + 1] == "R":
                    safe = False
            if i + 2 < m and j - 1 >= 0:
                if papan[i + 2][j - 1] == "R":
                    safe = False
            if i - 2 >= 0 and j - 1 >= 0:
                if papan[i - 2][j - 1] == "R":
                    safe = False

# Output
if safe == True:
    print("Raja aman dari serangan kuda.")
else: # safe == False
    print("Raja tidak aman dari serangan kuda.")