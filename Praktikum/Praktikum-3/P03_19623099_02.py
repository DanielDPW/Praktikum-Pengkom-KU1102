# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   19 Oktober 2023
# Deskripsi :   Bilangan prima

# KAMUS
# N         :   int
# arr       :   list
# y         :   int
# arr2      :   list
# pot       :   int
# n         :   int
# k         :   int

# ALGORITMA
# Input
N = int(input("Masukkan nilai N: "))
arr = [0 for i in range(N)]
for i in range(N):
    arr[i] = int(input(f"Masukkan bilangan ke-{i + 1}: "))

# Proses
n = 0
pot = 0
y = int((N / 2) * (1 + N))
arr2 = [0 for i in range(y + 1)]

for i in range(N):
    for j in range(i, N):
        arr2[n] = arr2[n] + arr[j]
        arr2[n + 1] = arr2[n]
        n = n + 1
    arr2[n] = 0
print(arr2)

for i in range(y):
    k = 2
    prima =  True
    while k <= arr2[i]**0.5 and prima == True:
        if arr2[i] % k == 0:
            prima = False
        k = k + 1
    if arr2[i] == 1:
        prima = False
    if prima == True:
        pot = pot + 1
# Output
if pot == 0:
    print("Tidak terdapat potongan list yang jumlahnya prima.")
else:
    print(f"Terdapat {pot} potongan list yang jumlahnya prima.")