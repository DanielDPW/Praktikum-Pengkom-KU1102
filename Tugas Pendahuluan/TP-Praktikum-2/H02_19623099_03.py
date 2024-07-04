# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   29 September 2023
# Deskripsi :   Program Perkalian Bergantian

# KAMUS
# A         :   int
# B         :   int
# N         :   int
# A0        :   int
# B0        :   int
# Repeated  :   boolean
# Nilai     :   int
# temp      :   int

# ALGORITMA
# Input
A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))
N = int(input("Masukkan nilai N: "))

# Proses
Nilai = A 
A0 = A # Store nilai variabel A dan B awal.
B0 = B
Repeated = False 
temp = 0 # Variabel pembantu dalam penukaran nilai A dan B
while (Nilai < N) and ((A * B) != 1) and ((A * B) != -1): 
    Nilai = Nilai * B
    temp = B
    B = A # Nilai variabel A dan B bertukar tempat
    A = temp
    if(Repeated == False) and (Nilai > N):
        Nilai = B0 
        A = B0 # Assign variabel A dan B dengan nilai awalnya namun nilai keduanya bertukar.
        B = A0
        Repeated = True # Boolean Repeated menjadi bernilai true artinya setelah ini akan sudah terulang sekali.

# Jika perkalian (A * B * A....) tidak memenuhi sehingga Nilai melebihi N,
# kondisi While looping di awal terpenuhi lagi karena nilai diassign dengan nilai B0.
# Setelah proses loop kedua tersebut selesai, keluar hasil jika Nilai == N.

# Output
if(Nilai == N) and ((A * B)<= N):
    print(f"Bilangan {N} dapat dicapai.")
else: # (Nilai != N) or ((A * B) > N)
    print(f"Bilangan {N} tidak dapat dicapai.")