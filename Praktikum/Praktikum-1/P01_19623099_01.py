# NIM       :   19623099
# Tanggal   :   21 September 2023
# Deskripsi :   Membandingkan nilai mata uang Peng dan mata uang Kom

# KAMUS
# Peng      :   integer
# Kom       :   integer
# KPeng     :   integer
# KKom      :   integer
# NilaiPeng :   integer
# NilaiKom  :   integer
# Pilihan   :   string

# ALGORITMA
# Input
Peng = int(input("Banyak uang Peng yang ditawarkan: "))
Kom = int(input("Banyak uang Kom yang ditawarkan: "))
KPeng = int(input("Konversi mata uang Peng ke rupiah: "))
KKom = int(input("Konversi mata uang Kom ke rupiah: "))

# Proses
NilaiPeng = Peng * KPeng
NilaiKom = Kom * KKom

if(Peng >= 0) and (Kom >= 0) and (KPeng >= 0) and (KKom >= 0):
    if(NilaiPeng > NilaiKom):
        Pilihan = "Peng"
    elif(NilaiPeng < NilaiKom):
        Pilihan = "Kom"
    elif(NilaiPeng == NilaiKom):
        Pilihan = "Sama"
        # Jika sama maka tidak pengaruh dia ambil apa
else: # (Peng < 0) or (Kom < 0) and (KPeng < 0) and (KKom < 0)
    Pilihan = "Invalid"

# Output
if(Pilihan != "Invalid") and (Pilihan != "Sama"):
    print(f"Adik Tuan Kil memilih uang {Pilihan}.")
elif(Pilihan != "Invalid") and (Pilihan == "Sama"):
    print("Keduanya bernilai sama.")
else: # Pilihan == "Invalid"
    print("Input tidak valid.")