def jumlah(a,b):
    c = a + b
    return c

hasil = jumlah(4,5)
print(hasil)


# lambda function untuk mempermudah seperti fungsi di atas

# misal, membuat anonymous function dengan lambda
kali = lambda argumen: print(argumen)
kali('test')
