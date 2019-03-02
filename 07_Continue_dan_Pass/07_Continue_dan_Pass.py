# continue
for i in range(1, 10):
    if i is 6:
        print('nilai i adalah ', 6)
        continue    # fungsinya untuk melanjutkan ke step selanjutnya

    print('nilai saai ini adalah ',i)
else:
    print('akhir dari loop')

print('akhir di LUAR loop CONTINUE\n')

# continue
for i in range(1, 10):
    if i is 6:
        print('nilai i adalah ', 6)
        pass    # hanya dilewat aja, tidak mempengaruhi apa2, bisa di buat jadi dummi

    print('nilai saai ini adalah ',i)
else:
    print('akhir dari loop')

print('akhir di LUAR loop PASS\n')
