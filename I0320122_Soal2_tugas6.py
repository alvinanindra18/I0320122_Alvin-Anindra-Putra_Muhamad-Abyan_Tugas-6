#soal2
Datasaya = int(input("Banyak data : "))
Listnilaisaya = []
i = 1
while i <= Datasaya:
    Nilai = int(input("Nilai Anda : "))
    Listnilaisaya.append(Nilai)
    i = i + 1
NilaiRata = sum(Listnilaisaya)/Datasaya
print("Rata-rata rapot Anda adalah", NilaiRata)