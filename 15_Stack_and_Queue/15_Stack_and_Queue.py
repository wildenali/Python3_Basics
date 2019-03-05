# perbedaan stack dan queue
# stack itu tumpukan
# queue itu antrian


# Stack - Contoh
print('======= # Stack - Contoh =======')
tumpukan = [1,2,3,4,5,6]
print('data sekarang', tumpukan)

# memasukan data baru
tumpukan.append(8)
print('data masuk', 8)
tumpukan.append(9)
print('data masuk', 9)
print('data sekarang', tumpukan)

# teknik stacking
out = tumpukan.pop()  # menghilangkan data paling belakang
print('data keluar', out)
print('data sekarang', tumpukan)


# Queue - Contoh
from collections import deque
print('\n======= # Queue - Contoh =======')
antrian = deque([1,2,3,4,5])      # tipe data deque
print('data sekarang', antrian)

# menambahkan data
antrian.append(6)
print('data masuk', 6)
print('data sekarang', antrian)

# menambahkan data
antrian.append(7)
print('data masuk', 7)
print('data sekarang', antrian)

# mengurangi antrian
out = antrian.popleft()
print('data keluar', out)
print('data sekrang', antrian)

# mengurangi antrian
out = antrian.popleft()
print('data keluar', out)
print('data sekrang', antrian)

# mengurangi antrian
out = antrian.popleft()
print('data keluar', out)
print('data sekrang', antrian)

# menambahkan data
antrian.append(8)
print('data masuk', 8)
print('data sekarang', antrian)
