# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   26 Oktober 2023
# Deskripsi :   Reproduksi bakteri Pengkombacter

# KAMUS
# N, K, amt, maks : int

# Fungsi Reproduksi
def Reproduksi(x, y, z):
    # Menghitung jumlah bakteri setelah bereproduksi z kali

    # KAMUS LOKAL
    # x, y, z : int

    # ALGORITMA
    for i in range(z):
        x = x * 2 + y
    return x

# ALGORITMA
# Input
N = int(input("Masukkan N: "))
K = int(input("Masukkan K: "))
amt = N # Simpan nilai variabel N awal.

# Proses
maks = Reproduksi(N, amt, K) # Masukkan nilai N, K, dan amt ke dalam fungsi Reproduksi

# Output
print(f"Terdapat {maks} Bakteri Pengkombacter.")