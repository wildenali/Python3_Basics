#usr/bin/python3

# https://belajarpython.com/tutorial/list-python

Data = [1, 4, 9, 16, 26, 4 ,56, 88]
print(Data)     # [1, 4, 9, 16, 26, 4, 56, 88]

# Akses List
Subdata1 = Data[4]  # ambil data ke 4 dari kiri
Subdata2 = Data[-2] # ambil data ke 2 dari kanan
print(Subdata1)     # 26
print(Subdata2)     # 56

# Potong List
Subdata3 = Data[2:4]    # 2  sampai sebelum 4
Subdata4 = Data[2:]
Subdata5 = Data[:2]
Subdata6 = Data[:-3]    # potong 3 buah data dari belakang
print(Subdata3)     # [9, 16]
print(Subdata4)     # [9, 16, 26, 4, 56, 88]
print(Subdata5)     # [1, 4]
print(Subdata6)     # [1, 4, 9, 16, 26]

# Tambah List
Data2 = [100, 200, 300, 400, 500, 600, 700, 800]
Data3 = Data + Data2
print(Data3)        # [1, 4, 9, 16, 26, 4, 56, 88, 100, 200, 300, 400, 500, 600, 700, 800]

# Mengubah Data
print(Data)         # [1, 4, 9, 16, 26, 4, 56, 88]
Data[4] = 999
print(Data)         # [1, 4, 9, 16, 999, 4, 56, 88]

# Mengcopy list ke variable baru
a = Data[:]
a[2] = 6666

# Merubah content list dengan menggunkana metoda slicing
Data[3:5] = [11, 12]
print(Data)         # [1, 4, 9, 11, 12, 4, 56, 88]

# List dalam List
x = [Data, Data2]
print(x)            # [[1, 4, 9, 11, 12, 4, 56, 88], [100, 200, 300, 400, 500, 600, 700, 800]]

# Mengakses Multidimensional List
y = x[0][1]         # [komponen pertama][isi list komponen pertama]
print(y)            # 4

# methods untuk menambahkan angka di akhir list
Data.append(30)
print(Data)         # [1, 4, 9, 11, 12, 4, 56, 88, 30]
Data.append(Data2)
print(Data)         # [1, 4, 9, 11, 12, 4, 56, 88, 30, [100, 200, 300, 400, 500, 600, 700, 800]]

# Funciton yang bisa digunakan kepada List
panjang_list = len(Data)
print(panjang_list) # 10
