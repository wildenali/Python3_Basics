# berguna untuk dapat mengubah variable dan atau untuk dapat memproteksi sebuah variable

# scope variable : local
print('# scope variable : local')
namaKucing = 'casandra'
def ubahNamaKucing(namaBaru):
    namaKucing = namaBaru
    print('saya ubah nama kucing menjadi', namaKucing)

ubahNamaKucing('ketie')
print('nama kucing saya menjadi', namaKucing)



# scope variable : global
print('\n# scope variable : global')

namaKucing = 'casandra'
makananKucing = 'royal canin'
def ubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('saya ubah nama kucing menjadi', namaKucing)

def kasihMakanKucing(makanan, nama):
    global namaKucing, makananKucing
    namaKucing = nama
    makananKucing = makanan

ubahNamaKucing('ketie')

kasihMakanKucing('universal','alex')

print('nama kucing saya menjadi', namaKucing,'dan makan',makananKucing)
