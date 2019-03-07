# cara input dan output file contoh .txt



"""
mode dalam membuat file
w = write mode -> mode menulis dan menghapus file lama, jika file tidak ada, maka akan di buat file baru
r = read mode only -> hanya bisa baca
a = appending mode -> menambahkan data di akhir baris
r+ = write dan read mode
"""

# MEMBUAT file
file = open("data.txt", 'w')
file.write("ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")
file.close()    # setelah open jangan lupa close, supaya tersimpan


# MEMBACA file text
file2 = open("data.txt",'r')
# print(file2.read())
# print(file2.read(10))       # 10 adalah jumlah karakter
print(file2.readline())     # baca sebaris
file2.close()


# APPENDING mode
file3 = open("data.txt",'a')
file3.write("\nbaris ini dibuat dengan menggunakan mode APPEND")
file3.close()
