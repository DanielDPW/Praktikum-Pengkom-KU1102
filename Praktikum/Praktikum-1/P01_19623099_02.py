# NIM       :   19623099
# Tanggal   :   21 September 2023
# Deskripsi :   Mencari angka spesial 

# KAMUS
# Angka     :   integer
# Angka1    :   integer
# Angka2    :   integer
# Angka3    :   integer
# Angka4    :   integer
# Hasil     :   string

# ALGORITMA
# Input
Angka = int(input("Masukkan Angka: "))
# Proses
if(1000 <= Angka <= 9999):
    Angka1 = Angka // 1000 
    Angka2 = (Angka // 100) - (Angka1 * 10)
    Angka3 = (Angka // 10) - (Angka1 * 100) - (Angka2 * 10)
    Angka4 = (Angka) - (Angka1 * 1000) - (Angka2 * 100) - (Angka3 * 10)
    if ((Angka2 + Angka3) != 0) and ((Angka1 * Angka4) % (Angka2 + Angka3) == 0):
        Hasil = "adalah angka spesial"
    else: # (Angka1 * Angka4) % (Angka2 + Angka3) != 0
        Hasil = "bukan angka spesial"
else: # Angka < 1000 atau Angka > 9999
    Hasil = "Invalid"

# Output
if(Hasil != "Invalid"):
    print(f"Angka {Angka} {Hasil}.")
else: #(Hasil == "Invalid")
    print("Input tidak valid.")