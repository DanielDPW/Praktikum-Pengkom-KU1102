# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   9 Oktober 2023
# Deskripsi :   Program Menghitung Kehadiran

# KAMUS
# N         :   int
# M         :   int
# H         :   int
# arr       :   list

# ALGORITMA
# Input
N = int(input("Masukkan nilai N: "))
while (N < 1):
    N = int(input("Masukkan nilai N: ")) # Ini memastikan input yang dimasukkan tepat
M = int(input("Masukkan nilai M: "))
while (M > N) or (M < 0):
    M = int(input("Masukkan nilai M: ")) # Ini memastikan input yang dimasukkan tepat

# Proses
arr = [i + 1 for i in range(N)] # Membuat array dari 1 hingga N

for j in range(1, M + 1):
    H = int(input(f"Masukkan data ke-{j}: "))
    while (H > N) or (H < 1) or (arr[H - 1] == 0):
        H = int(input(f"Masukkan data ke-{j}: "))
    arr[H - 1] = 0 # Data di indeks H - 1 akan diubah menjadi 0

# Output
if(N > M):
    print("Nomor perwakilan yang tidak datang: ", end = '')
    for k in range(1, N + 1):
        if (arr[k - 1] != 0):
            print(f"{arr[k - 1]} ", end = '') # Array yang tidak bernilai 0 akan diprint
else: # N == M
    print("Semua perwakilan hadir. ")