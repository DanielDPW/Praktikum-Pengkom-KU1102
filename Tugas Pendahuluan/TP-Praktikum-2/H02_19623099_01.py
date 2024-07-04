# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   29 September 2023
# Deskripsi :   Program Menentukan Perpangkatan

# KAMUS
# N         :   int
# k         :   int
# Hasil     :   int

# ALGORITMA
# Input
N = int(input("Masukkan bilangan N: "))
k = int(input("Masukkan bilangan k: "))

# Proses
Hasil = k
while (Hasil < N):
    Hasil = Hasil * k

# Output
if(Hasil == N):
    print(f"{N} merupakan perpangkatan {k}.")
else: # Hasil != N
    print(f"{N} bukan merupakan perpangkatan {k}.")