# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   19 Oktober 2023
# Deskripsi :   Total minimal harga pembayaran di restoran yang unik.

# KAMUS
# N         :   int
# harga     :   list
# mulai     :   list
# min       :   float

# ALGORITMA
# Input
N = int(input("Masukkan nilai N: "))

harga = [0 for i in range(N)]
mulai = [0 for i in range(N - 2)]

for i in range(N):
    harga[i] = float(input(f"Masukkan harga jam ke-{i + 1}: "))

# Proses
min = harga[0] + harga[1] + harga[2]
for i in range(N - 2):
    if (N - i) >= 3:
        mulai[i] = harga[i] + harga[i + 1] + harga[i + 2]
        if mulai[i] < min:
            min = mulai[i]

# Output
print(f"Total harga yang harus dibayar adalah {min}")