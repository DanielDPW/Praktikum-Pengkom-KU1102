# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   9 Oktober 2023
# Deskripsi :   Program Stasiun Terbanyak

# KAMUS
# x         :   int
# y         :   int
# z         :   int
# l         :   int
# M         :   int
# N         :   int
# arr       :   list
# arr2      :   list

# ALGORITMA
# Input
x = int(input("Masukkan uang yang dibawa Tuan Leo: "))
while (x < 0):
    x = int(input("Masukkan uang yang dibawa Tuan Leo: ")) # Ini memastikan input yang dimasukkan tepat
y = int(input("Masukkan jumlah stasiun: "))
while (y < 1):
    y = int(input("Masukkan jumlah stasiun: ")) # Ini memastikan input yang dimasukkan tepat

# Proses
arr = [0 for i in range(2 * y)] # Mendeclare array sepanjang 2 * y
arr2 = [0 for a in range(y)] # Mendeclare array sepanjang y
for j in range(y):
    z = int(input(f"Masukkan harga stasiun ke-{j + 1}: "))
    while z < 0:
        z = int(input(f"Masukkan harga stasiun ke-{j + 1}: "))
    arr[j] = z
    arr[j + y] = z
    # Memasukkan nilai ke dalam array

M = 0
N = 0
for k in range(y):
    if(arr2[k] == 0) and (arr[k] <= x):
        arr2[k] = arr2[k] + 1
        if (M < arr2[k] <= y):
            M = arr2[k]
            N = k + 1
    # Mengecek apakah dia bisa masuk melewati stasiun awal
    l = k
    while ((l + 1) < 2 * y) and ((arr[k] + arr[l + 1]) <= x):
        arr[k] = arr[k] + arr[l + 1]
        arr2[k] = arr2[k] + 1
        l = l + 1
        if (M < arr2[k] <= y):
            M = arr2[k]
            N = k + 1
    # Mengecek apakah dia bisa masuk melewati stasiun berikutnya

# Output
if (N == 0):
    print("Tuan Leo kekurangan uang.")
else: # N != 0
    print (f"Tuan Leo dapat mengunjungi {M} stasiun dimulai dari stasiun ke-{N}.")