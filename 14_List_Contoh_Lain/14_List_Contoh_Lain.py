Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)
# ['kunci', 'ember', 'jaket', 'ban', 'mobil']

# method method yang dipakain untuk memanipulasi list
# menambah data ke dalam list
Barang.append('sepeda')
print(Barang)
# ['kunci', 'ember', 'jaket', 'ban', 'mobil', 'sepeda']

# meng ekstend, si dompet, dompet nya ter iterable
Barang.extend('dompet')
print(Barang)
# ['kunci', 'ember', 'jaket', 'ban', 'mobil', 'sepeda', 'd', 'o', 'm', 'p', 'e', 't'] 

# insert data
Barang.insert(3,'odong-odong')
Barang.insert(1,'sepeda')
print(Barang)
# ['kunci', 'sepeda', 'ember', 'jaket', 'odong-odong', 'ban', 'mobil', 'sepeda', 'd', 'o', 'm', 'p', 'e', 't']

# method untuk menghitung anggota data
jumlahSepeda = Barang.count('sepeda')
print('Jumlah Sepeda adalah:',jumlahSepeda)
# Jumlah Sepeda adalah: 2

# remove data
Barang.remove('sepeda')     # akan me remove data yang pertama kali ketemu
print(Barang)
# ['kunci', 'ember', 'jaket', 'odong-odong', 'ban', 'mobil', 'sepeda', 'd', 'o', 'm', 'p', 'e', 't']

# membalik posisi data didalam list
Barang.reverse()
print(Barang)
# ['t', 'e', 'p', 'm', 'o', 'd', 'sepeda', 'mobil', 'ban', 'odong-odong', 'jaket', 'ember', 'kunci']

Stuff = Barang
Stuff.append('gelas')
print(Stuff)
# ['t', 'e', 'p', 'm', 'o', 'd', 'sepeda', 'mobil', 'ban', 'odong-odong', 'jaket', 'ember', 'kunci', 'gelas']

print(Barang)   # kenapa barang juga ikut ter tambah, karena barang menggunakan referensi yang sama dengan stuff
# ['t', 'e', 'p', 'm', 'o', 'd', 'sepeda', 'mobil', 'ban', 'odong-odong', 'jaket', 'ember', 'kunci', 'gelas']

Stuff = Barang.copy()   # supaya normal caranya, disini pakai .copu() , jadi mengkopikan data si barang ke stuff
Stuff.append('gelas')
print(Stuff)
# ['t', 'e', 'p', 'm', 'o', 'd', 'sepeda', 'mobil', 'ban', 'odong-odong', 'jaket', 'ember', 'kunci', 'gelas', 'gelas']

print(Barang)
# ['t', 'e', 'p', 'm', 'o', 'd', 'sepeda', 'mobil', 'ban', 'odong-odong', 'jaket', 'ember', 'kunci', 'gelas']
