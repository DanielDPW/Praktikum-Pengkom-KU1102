# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   9 Oktober 2023
# Deskripsi :   Program Angka Terbesar ke-N

# KAMUS
# x         :   int
# N         :   int
# arr       :   list
# arr2      :   list

# ALGORITMA
# Input
x = int(input("Masukkan banyak data: "))
while (x < 1):
    x = int(input("Masukkan banyak data: "))
N = int(input("Masukkan nilai N: "))
while (N > x):
    N = int(input("Masukkan nilai N: "))

# Proses
arr = [0 for i in range(x)]

for j in range(x):
    arr[j] = int(input(f"Masukkan data ke-{j + 1}: "))

for a in range(x - 1):
    for b in range(a + 1, x):
        if arr[a] < arr[b]:
            temp = arr[b]
            arr[b] = arr[a]
            arr[a] = temp
arr2 = []
arr2 = arr2 + arr

for a in range(x - 1):
    for b in range(a + 1, x):
        if arr2[a] == arr2[b]:
            arr2[b] = 0
        if arr2[b] > arr2[a]:
            temp = arr2[b]
            arr2[b] = arr2[a]
            arr2[a] = temp

# Output
if (arr2[N - 1] == 0) and (arr[N - 1] != 0):
    print("Tidak ada. ")
else:
    print(f"Nilai terbesar ke-{N} adalah {arr2[N - 1]}")