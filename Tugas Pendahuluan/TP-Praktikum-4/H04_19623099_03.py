# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   26 Oktober 2023
# Deskripsi :   Banyak kapal negera musuh dari Negara Pengkom

# KAMUS
# N, M, count : int
# found : bool
# matriks : list of list of int

# ALGORITMA
# Input
N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))
print("Masukkan peta:")
matriks = [list(map(int, input()[0:M])) for i in range(N)]

# Proses
count = 0 # variabel untuk menghitung jumlah kapal musuh.
found = False # variabel untuk mencari apakah ketemu 0 atau tidak.

for i in range(N):
    for j in range(M):
        if matriks [i][j] == 1: # Periksa apakah matriks [i][j] bernilai 1
            for k in range(j + 1, M): # Periksa matriks-matriks di sampingnya (horizontal).
                if matriks[i][k] == 1 and found == False: # Bila bertemu satu, maka nilai matriks itu diubah menjadi nol.
                    matriks[i][k] = 0
                else: # Bila bertemu nol, maka loop di atas berhenti.
                    found = True
            found = False
            for l in range(i + 1, N): # Periksa matriks-matriks di bawahnya (vertikal).
                if matriks[l][j] == 1 and found == False: # Bila bertemu satu, maka nilai matriks itu diubah menjadi nol.
                    matriks[l][j] = 0
                else: # Bila bertemu nol, maka loop di atas berhenti.
                    found = True
            found = False
            count = count + 1 # Jumlah kapal yang telah terdeteksi akan bertambah.
            matriks[i][j] = 0 # Agar kapal tidak dideteksi ulang, nilai matriks [i][j] kita ubah menjadi
            
# Output
if count == 0:
    print("Tidak terdapat kapal musuh pada peta.")
else: # count != 0
    print(f"Terdapat {count} kapal musuh pada peta.")