# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   19 Oktober 2023
# Deskripsi :   Bilangan prima

# KAMUS
# N         :   int
# arr       :   list
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

for i in range(N):
    sum = 0
    for j in range(i, N):
        prima = True
        sum = sum + arr[j]
        k = 2
        while k <= sum ** 0.5 and prima == True:
            if sum % k == 0:
                prima = False
            k = k + 1
        
        if sum == 1:
            prima = False
        if prima == True:
            pot = pot + 1

# Output
if pot == 0:
    print("Tidak terdapat potongan list yang jumlahnya prima.")
else:
    print(f"Terdapat {pot} potongan list yang jumlahnya prima.")