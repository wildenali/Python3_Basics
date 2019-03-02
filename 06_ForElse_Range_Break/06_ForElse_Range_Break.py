# Range
print(range(10, 50, 5))         # ini bukan list, tapi class
for i in range(10, 50, 5):      # 5 adalah increment nya
    print(i)


# for else
# else untuk for
for i in range(0, 5):
    print(i)
else:
    print('halow')

# break
for i in range(0, 40):
    print(i)
    if i is 25:     # coba ubah 25 jadi 50
        print('angka ditemukan ', i)
        break
else:
    print('angka tidak ditemukan')
