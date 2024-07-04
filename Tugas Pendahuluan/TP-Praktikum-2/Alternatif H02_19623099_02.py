H = int(input("Masukkan nilai H: "))
Baris = 1
Kolom = 1
Hasil = 1
if((H % 2) == 0):
    Puncak = (1 / 2) * H
    while (Baris <= H):
        if(Baris < Puncak):
            while (Kolom <= Baris):
                print(f"{Hasil} ", end ='')
                Hasil = Hasil + 1
                Kolom = Kolom + 1
            Kolom = 1
            print()
        elif(Baris == Puncak):
            while (Kolom <= Baris):
                print(f"{Hasil} ", end = '')
                Hasil = Hasil + 1
                Kolom = Kolom + 1
            Kolom = 1
            BPuncak = Baris
            print()
        elif(Baris == (Puncak + 1)):
            while (Kolom <= BPuncak):
                print(f"{Hasil} ", end = '')
                Hasil = Hasil + 1
                Kolom = Kolom + 1
            Kolom = 1
            print()
        elif(Baris > (Puncak + 1)):
            BPuncak = BPuncak - 1
            while (Kolom <= BPuncak):
                print(f"{Hasil} ", end = '')
                Hasil = Hasil + 1
                Kolom = Kolom + 1
            Kolom = 1
            print()
        Baris = Baris + 1
if((H % 2) == 1):
    Puncak = (1 / 2) * (H + 1)
    while (Baris <= H):
        if(Baris < Puncak):
            while (Kolom <= Baris):
                print(f"{Hasil} ", end ='')
                Hasil = Hasil + 1
                Kolom = Kolom + 1
            Kolom = 1
            print()
        elif(Baris == Puncak):
            while (Kolom <= Baris):
                print(f"{Hasil} ", end = '')
                Hasil = Hasil + 1
                Kolom = Kolom + 1
            Kolom = 1
            BPuncak = Baris
            print()
        elif(Baris > Puncak):
            BPuncak = BPuncak - 1
            while (Kolom <= BPuncak):
                print(f"{Hasil} ", end = '')
                Hasil = Hasil + 1
                Kolom = Kolom + 1
            Kolom = 1
            print()
        Baris = Baris + 1