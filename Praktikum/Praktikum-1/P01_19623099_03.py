# NIM       :   19623099
# Tanggal   :   21 September 2023
# Deskripsi :   Menghitung jumlah baju berdasarkan kain dan pita

# KAMUS     
# Kain      :   float
# Pita      :   float
# KainL     :   float
# KainM     :   float
# KainS     :   float
# PitaL     :   float
# PitaM     :   float
# PitaS     :   float
# L         :   int
# M         :   int
# S         :   int

# ALGORITMA
# Input
Kain = float(input("Jumlah kain: "))
Pita = float(input("Jumlah pita: "))

# Proses
KainL = Kain - 2
KainM = KainL - 1.5
KainS = KainM - 1.2
# Kita mencari apakah kain cukup.

PitaL = Pita - 1.3
PitaM = PitaL - 1
PitaS = PitaM - 0.8
# Kita mencari apakah pita cukup.
if(KainS < 0) or (PitaS < 0):
    Bahan = "Tidak Cukup"
    # Jika salah satu saja tidak cukup, maka tentu saja tidak cukup.
else:
    Bahan = "Cukup"
    L = 1
    M = 1
    S = 1
    # Karena setidaknya satu masing-masing terbuat, maka semuanya setidaknya berjumlah satu
    Kain = KainS # Sisa kainnya akan ekuivalen dengan KainS
    Pita = PitaS # Sisa pitanya akan ekuivalen dengan PitaS
    KainL = Kain // 2 # Kita cari hasil bagi bulat
    PitaL = Pita // 1.3 # Kita cari hasil bagi bulat
    if(KainL <= PitaL):
        L = int(L + KainL)
    elif(KainL > PitaL):
        L = int(L + PitaL)
    # Kita cari berapa baju terbuat.
    KainL = 2 * (L-1) 
    PitaL = 1.3 * (L-1)
    # Sisa kain dan pita
    KainM = (Kain - KainL) // 1.5 # Kita cari hasil bagi bulat
    PitaM = (Pita - PitaL) // 1 # Kita cari hasil bagi bulat
    if(KainM <= PitaM):
        M = int(M + KainM)
    elif(KainM > PitaM):
        M = int(M + PitaM)
    # Kita cari berapa baju terbuat
    KainM = 1.5 * (M-1)
    PitaM = 1 * (M-1)
    # Sisa kain dan pita
    KainS = (Kain - KainL - KainM) // 1.2 # Kita cari hasil bagi bulat
    PitaS = (Pita - PitaL - PitaM) // 0.8 # Kita cari hasil bagi bulat
    if(KainS <= PitaS):
        S = int(S + KainS)
    elif(KainS > PitaS):
        S = int(S + PitaS)
    # Kita cari berapa baju terbuat

# Output
if(Bahan != "Tidak Cukup"):
    print(f"Nona Deb dapat membuat {S} ukuran S, {M} ukuran M, dan {L} ukuran L.")
else: # Bahan == "Tidak Cukup"
    print("Bahan tidak cukup untuk membuat baju.")