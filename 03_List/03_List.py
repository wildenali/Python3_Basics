#usr/bin/python3

# list itu kaya array, cuma cara penulisaanya bedad dengan array
# perbedaan nya apa dong


Data = [1, 4, 9, 16, 26, 4 ,56, 88]
Data2 = [100, 200, 300, 400, 500, 600, 700, 800]

# Akses List
Subdata1 = Data[4]
Subdata2 = Data[-2]

# Potong List
Subdata3 = Data[2:4]    # 2  sampai sebelum 4
Subdata4 = Data[2:]
Subdata5 = Data[:2]
Subdata6 = Data[:-3]    # potong 3 buah data dari belakang

# Tambah List
Data3 = Data + Data2;


print(Data)
print(Subdata1)
print(Subdata2)
print(Subdata3)
print(Subdata4)
print(Subdata5)
print(Subdata6)

print(Data3)

# Mengubah Data
print(Data)
Data[4] = 999;
print(Data)

# Mengcopy list ke variable baru
a = Data[:]
a[2] = 6666

# Merubah content list dengan menggunkana metoda slicing
Data[3:5] = [11, 12]
print(Data)


# List dalam List
x = [Data, Data2]
print(x)

# Mengakses Multidimensional List
y = x[0][1]     # [komponen pertama][isi list komponen pertama]
print(y)


# methods untuk list
Data.append(30)
print(Data)
Data.append(Data2)
print(Data)

# Funciton yang bisa digunakan kepada List
panjang_list = len(Data)
print(panjang_list)
