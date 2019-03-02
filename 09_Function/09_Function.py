# mendefinisikan fungsi
def fungsi():
    print('ini adalah fungsi')

def suaraayam():
    print('kukuruyuk')

def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah 20k')


# memanggil fungsi
fungsi()
fungsi()
fungsi()
hargaayam()

print('\n# membuat fungsi dengan input argumen')
# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargaTotal = kg * harga
    print('harga', kg, 'kg ayam adalah', hargaTotal)

hargatotalayam(2)
hargatotalayam(1)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(65)
