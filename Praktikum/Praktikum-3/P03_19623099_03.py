# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   19 Oktober 2023
# Deskripsi :   Mendeteksi apakah Komi telah mengucapkan suatu kata dengan benar

# KAMUS
# N         :   int
# M         :   str
# x         :   int
# Komi      :   bool
# y         :   int
# z         :   str
# arr       :   list
# n         :   int

# ALGORITMA
# Input
N = int(input("Masukkan panjang kata asli: "))
M = str(input("Masukkan kata asli: "))
x = int(input("Masukkan jumlah kata yang ditulis: "))
z = str(input("Masukkan kata yang ditulis: "))
y = int((N / 2) * (1 + N))
Komi = True
arr = ["" for i in range(y)]

# Proses
n = 0
for i in range(1, N + 1):
    for j in range(i):
        arr[n] = M[j]
        n = n + 1
if x == y:
    for i in range(y):
        if arr[i] != z[i]:
            Komi = False

# Output
if x != y:
    print("Tulisan Komi masih salah.")
else:
    if Komi == True:
        print("Tulisan Komi sudah benar.")
    else:
        print("Tulisan Komi masih salah.")
