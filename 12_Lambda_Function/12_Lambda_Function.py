def jumlah(a,b):
    c = a + b
    return c

hasil = jumlah(4,5)
print(hasil)


# lambda function untuk mempermudah seperti fungsi di atas

# misal, membuat anonymous function dengan lambda
kali = lambda argumen: print(argumen)
kali('test')

kali = lambda x,y: x*y
print(kali(3,4))
