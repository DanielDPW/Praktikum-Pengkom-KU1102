# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   29 September 2023
# Deskripsi :   Program Segitiga Sama Kaki Angka

# KAMUS
# H         :   int
# Baris     :   int
# Kolom     :   int
# Angka     :   int

# ALGORITMA
# Input
H = int(input("Masukkan nilai H: "))

# Proses
Baris = 1
Angka = 1
while (Baris <= H / 2): # H / 2 adalah puncak dari segitiga
    for Kolom in range(1, Baris + 1): # Range mulai dari 1 ke baris saat itu juga.
        print(f"{Angka} ", end='')
        Angka = Angka + 1
    Baris = Baris + 1 # Pindah ke baris berikutnya.
    print()
while (Baris <= H): # Setelah While loop sebelumnya selesai, While loop baris dari puncak ke akhir.
    for Kolom in range(Baris, H + 1): # Karena baris bertambah banyak, range yang diprint semakin sedikit.
        print(f"{Angka} ", end ='')
        Angka = Angka + 1 
    Baris = Baris + 1 # Pindah ke baris berikutnya.
    print()