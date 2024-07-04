A = int(input("Masukkan Input A: "))
B = int(input("Masukkan Input B: "))
N = int(input("Masukkan Input N: "))

Nilai = A
Hasil = 0
Run = 1
while (Nilai < N):
    Nilai = Nilai * B
    if(Nilai == N):
        Hasil = Nilai
        break
    Nilai = Nilai * A
    if(Nilai == N):
        Hasil = Nilai
        break
    if (Nilai > N & Run == 1):
        Nilai = B
        temp = A
        A = B
        B = temp
        Run = 0
if(Hasil == N):
    print(f"Bilangan {N} dapat dicapai.")
else:
    print(f"Bilangan {N} tidak dapat dicapai.")