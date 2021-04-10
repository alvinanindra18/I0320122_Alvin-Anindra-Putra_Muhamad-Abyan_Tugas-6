#soal 2
print("=====Menghitung nilai rata-rata=====")
BanyakData = int(input("Banyak data: "))
data = []
jumlah = 0
for nilai in range(0, BanyakData):
    temp = int(input("Masukkan data ke-%d: " % (nilai + 1)))
    data.append(temp)
    jumlah += data[nilai]
    RataRata = jumlah / BanyakData
print("Rata-ratanya adalah: ", RataRata)

