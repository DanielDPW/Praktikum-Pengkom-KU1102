# NIM/Nama  :   19623099/Daniel Pedrosa Wu
# Tanggal   :   12 September 2023
# Deskripsi :   Program Menghitung Kemiringan Garis

# KAMUS
# x1        :   float
# y1        :   float
# x2        :   float
# y2        :   float
# m         :   float
# Garis     :   string

# ALGORITMA
# Input
x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

# Proses
if(x1 == x2) and (y1 != y2):
    Garis = "termasuk garis vertikal"
elif(y1 == y2) and (x1 != x2):
    Garis = "termasuk garis horizontal"
elif(x1 == x2) and (y1 == y2):
    Garis = "tidak terdefinisi"
else: # x1 != x2 and y1 != y2 
    m = (y2 - y1)/(x2 - x1)
    Garis = (f"memiliki gradien {m}")

# Output
print(f"Garis tersebut {Garis}.")
