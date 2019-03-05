Barang = ['kunci','ember','jaket','ban','mobil']
print(Barang)

# method method yang dipakain untuk memanipulasi list
# menambah data ke dalam list
Barang.append('sepeda')
print(Barang)

# meng ekstend, si dompet, dompet nya ter iterable
Barang.extend('dompet')
print(Barang)

# insert data
Barang.insert(3,'odong-odong')
Barang.insert(1,'sepeda')
print(Barang)

# method untuk menghitung anggota data
jumlahSepeda = Barang.count('sepeda')
print('Jumlah Sepeda adalah:',jumlahSepeda)

# remove data
Barang.remove('sepeda')     # akan me remove data yang pertama kali ketemu
print(Barang)

# membalik posisi data didalam list
Barang.reverse()
print(Barang)

Stuff = Barang
Stuff.append('gelas')
print(Stuff)
print(Barang)   # kenapa barang juga ikut ter tambah, karena barang menggunakan referensi yang sama dengan stuff

Stuff = Barang.copy()   # supaya normal caranya, disini pakai .copu() , jadi mengkopikan data si barang ke stuff
Stuff.append('gelas')
print(Stuff)
print(Barang)
