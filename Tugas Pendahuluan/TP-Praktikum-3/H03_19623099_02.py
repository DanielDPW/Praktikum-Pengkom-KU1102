# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   9 Oktober 2023
# Deskripsi :   Program Angka Terbesar ke-N

# KAMUS
# x         :   int
# N         :   int
# arr       :   list

# ALGORITMA
# Input
x = int(input("Masukkan banyak data: "))
while (x < 1):
    x = int(input("Masukkan banyak data: ")) # Ini memastikan input yang dimasukkan tepat
N = int(input("Masukkan nilai N: "))
while (N > x) or (N < 1):
    N = int(input("Masukkan nilai N: ")) # Ini memastikan input yang dimasukkan tepat

# Proses
arr = [0 for i in range(x)] # Declare array dengan panjang x

for j in range(x):
    arr[j] = int(input(f"Masukkan data ke-{j + 1}: ")) # Assign data ke dalam array

for a in range(x - 1):
    for b in range(a + 1, x):
        if arr[a] < arr[b]:
            temp = arr[b]
            arr[b] = arr[a]
            arr[a] = temp
# Mengurutkan data dalam array dari terbesar ke terkecil

# Output
print(f"Nilai terbesar ke-{N} adalah {arr[N - 1]}")