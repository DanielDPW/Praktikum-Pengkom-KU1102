# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   12 September 2023
# Deskripsi :   Program Harga Tiket Pesawat

# KAMUS
# Nomor     :   integer
# Posisi    :   string
# Kursi     :   string
# Harga     :   integer

# ALGORITMA
# Input
Nomor = int(input("Tentukan nomor kursi: "))
Posisi = str(input("Tentukan posisi kursi: "))

# Proses
if(1 <= Nomor <= 100) and ((Posisi == "A") or (Posisi == "B") or (Posisi == "C") or (Posisi == "D") or (Posisi == "E") or (Posisi == "F")): # Memeriksa apakah nomor dan posisi kursi valid.
    if(1 <= Nomor <= 20) or (51 <= Nomor <= 60):
        Kursi = "Hot Seat" # Nomor kursi 1-20 atau 51-60 kursinya diassign Hot Seat.
    elif(21 <= Nomor <= 50) or (61 <= Nomor <= 100):
        Kursi = "Reguler" # Nomor kursi 21-50 atau 61-100 kursinya diassign Reguler.

    if(Kursi == "Hot Seat"):
        if(Posisi == "A") or (Posisi == "F"):
            Harga = 1600000
        elif(Posisi == "B") or(Posisi == "E"):
            Harga = 1550000
        elif(Posisi == "C") or (Posisi == "D"):
            Harga = 1500000
    elif(Kursi == "Reguler"):
        if(Posisi == "A") or (Posisi == "F"):
            Harga = 1000000
        elif(Posisi == "B") or (Posisi == "E"):
            Harga = 950000
        elif(Posisi == "C") or (Posisi == "D"):
            Harga = 900000
else: # Nomor atau Posisi tidak valid
    Kursi = ""
    Harga = ""
# Output
if(Kursi != "") and (Harga != ""):
    print(f"Tuan Kil memilih kursi {Kursi} dengan harga {Harga}.")
else: # Kursi atau Harga tidak terdefinisi.
    print("Mohon masukkan nomor atau posisi kursi (ditulis kapital) yang benar.")