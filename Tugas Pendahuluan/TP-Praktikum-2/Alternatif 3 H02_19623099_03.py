A1 = int(input("Masukkan bilangan A: "))
B1 = int(input("Masukkan bilangan B: "))
N = int(input("Masukkan bilangan N: "))

A2 = A1
B2 = B1
Nilai1 = A1
Nilai2 = B1
temp = 0
while (Nilai1 < N):
    Nilai1 = Nilai1 * B1
    temp = B1
    B1 = A1
    A1 = temp
while (Nilai2 < N):
    Nilai2 = Nilai2 * A2
    temp = A2
    A2 = B2
    B2 = temp
if(Nilai1 == N) or (Nilai2 == N):
    print(f"Bilangan {N} dapat dicapai.")
else:
    print(f"Bilangan {N} tidak dapat dicapai.")