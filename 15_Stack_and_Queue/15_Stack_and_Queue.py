# perbedaan stack dan queue
# stack itu tumpukan
# queue itu antrian


# Stack - Contoh
print('======= # Stack - Contoh =======')
tumpukan = [1,2,3,4,5,6]
print('data sekarang', tumpukan)        # data sekarang [1, 2, 3, 4, 5, 6]

# memasukan data baru
tumpukan.append(8)
print('data masuk', 8)                  # data masuk 8
tumpukan.append(9)
print('data masuk', 9)                  # data masuk 9
print('data sekarang', tumpukan)        # data sekarang [1, 2, 3, 4, 5, 6, 8, 9]

# teknik stacking
out = tumpukan.pop()  # menghilangkan data paling belakang
print('data keluar', out)               # data keluar 9
print('data sekarang', tumpukan)        # data sekarang [1, 2, 3, 4, 5, 6, 8]


# Queue - Contoh
from collections import deque
print('\n======= # Queue - Contoh =======')
antrian = deque([1,2,3,4,5])      # tipe data deque
print('data sekarang', antrian)         # data sekarang deque([1, 2, 3, 4, 5])

# menambahkan data
antrian.append(6)
print('data masuk', 6)                  # data masuk 6
print('data sekarang', antrian)         # data sekarang deque([1, 2, 3, 4, 5, 6])

# menambahkan data
antrian.append(7)
print('data masuk', 7)                  # data masuk 7
print('data sekarang', antrian)         # data sekarang deque([1, 2, 3, 4, 5, 6, 7])

# mengurangi antrian
out = antrian.popleft()
print('data keluar', out)               # data keluar 1
print('data sekrang', antrian)          # data sekrang deque([2, 3, 4, 5, 6, 7])

# mengurangi antrian
out = antrian.popleft()
print('data keluar', out)               # data keluar 2
print('data sekrang', antrian)          # data sekrang deque([3, 4, 5, 6, 7])

# mengurangi antrian
out = antrian.popleft()
print('data keluar', out)               # data keluar 3
print('data sekrang', antrian)          # data sekrang deque([4, 5, 6, 7])

# menambahkan data
antrian.append(8)
print('data masuk', 8)                  # data masuk 8
print('data sekarang', antrian)         # data sekarang deque([4, 5, 6, 7, 8])
