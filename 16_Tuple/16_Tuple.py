# tipe data tuple

# List
Ganjil = [1,3,5,7,9]
print(Ganjil)

# Tuple -> tuple ini datanya FIX, maksudnya tidak dapat diubah, baik diTAMBAH, diKURANGAIn, atau DIUBAH
Genap = (2,4,6,8,10)
print(Genap)

# Cara cek list atau Tuple
print(type(Ganjil))
print(type(Genap))

Ganjil[2] = 99
Genap[2] == 69
print(Ganjil)
print(Genap)


# Cara mencari tau bisa ngapain aja dengan tipe data tertentu, caranya adalah dengan dir(data)
# print(dir(Ganjil))
print(dir(Genap))
print(Genap.index(6))

print('\n')

# cek besarnya data list dan tuple
import sys
data_list = [1,2,3,4,5,'ayam goreng','pisang goreng']
data_tuple = (1,2,3,4,5,'ayam goreng','pisang goreng')
besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)
print("besar data list:", besar_datalist)
print("besar data tuple:", besar_datatuple)

print('\n')

# cek WAKTU nya antara data list dan tuple
import timeit
data_list = timeit.timeit(stmt="[1,2,3,4,5,'ayam goreng','pisang goreng']",number=1000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,'ayam goreng','pisang goreng')",number=1000000)
print("waktu data list:", data_list)
print("waktu data tuple:", data_tuple)
# Jadi TUPLE UNTUK APA??????
# ya untuk data2 yang tidak perlu berubah-ubah
# tuple ini lebih ringan dari list ukuran size nya
