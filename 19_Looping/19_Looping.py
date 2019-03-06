# teknik looping
# enumerate
# zip


nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena',
             'Syahrini']

kumpulan_lagu = ['Akad',
        'Jona Nyaman',
        'Rumahku',
        'Sang Filsuf',
        'Sindoro']

# enumerate
for i,band in enumerate(nama_band):
    print(i,':',band)

print()

# enumerate dengan awalan nya 1 bukan 0
for i,band in enumerate(nama_band, start = 1):
    print(i,':',band)

print()

# zip -> menggabungkan list
for band,lagu in zip(nama_band, kumpulan_lagu):
    print(band,'menyanyikan lagu yang berjudul: ', lagu)

print()

# looping set
playlist = {'baby baby', 'ada dengan cinta', 'cenat cenut', 'jaran goyang'}

for lagu in sorted(playlist):
    print(lagu)

print()

# looping dictionary
playlist2 = {'Payung Teduh':'Akad',
             'Fourtwnty':'Zona Nyaman',
             'Dialog Dini Hari':'Rumahku',
             }
for i in playlist2.keys():
    print(i)
print()
for i in playlist2.values():
    print(i)
print()
for i in playlist2.items():
    print(i)

print()

for i in reversed(range(1,10,1)):
    print(i)
