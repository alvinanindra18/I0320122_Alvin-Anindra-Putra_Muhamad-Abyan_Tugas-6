#soal3
for b in range(10,25):
    for d in range(2, b):
        if (b % d) == 0:
            print(b, 'bukan prima')
            break
    else:
        print(b, 'adalah bilangan prima')