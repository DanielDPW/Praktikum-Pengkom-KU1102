A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))
N = int(input("Masukkan nilai N: "))

Nilai = A
Repeat = 0
Switch = 0
while (Nilai < N) and (Nilai != N) and ((A * B) != 1) and ((A * B) != -1):
    Nilai = Nilai * B
    temp = B
    B = A
    A = temp
    Switch = Switch + 1
    if(Repeat != 1) and (Nilai > N):
        if((Switch % 2) == 0):
            Nilai = B
            temp = B
            B = A
            A = temp
        elif((Switch % 2) == 1):
            Nilai = A
        Switch = 0
        Repeat = 1
if(Nilai == N) and (A < N) and (B < N):
    print(f"Bilangan {N} dapat dicapai.")
else:
    print(f"Bilangan {N} tidak dapat dicapai.")