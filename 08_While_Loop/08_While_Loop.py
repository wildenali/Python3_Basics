angka = 0

while angka < 5:
    print('nilai angka adalah', angka)
    angka = angka + 1

print('di LUAR while')

start = True
angka = 0
while start:
    print("ini dalam While")
    if angka is 100:
        start = False
        print('oke angka 100 ditemukan')
    angka += 1

print("\n")
print("# else, break, continue, pass")
# else, break, continue, pass
angka = 0
while angka < 10:
    if angka is 5:
        print('checkpoint 1')
        break
        print('checkpoint 2')

    print('nilai angka adalah: ', angka)
    angka += 1
else:
    print('nilai angka diakhir while adalah ', angka)
