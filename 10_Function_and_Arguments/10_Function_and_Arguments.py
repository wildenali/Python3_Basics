# fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print('siswa ini bernama', nama)

siswa('mario')

# fungsi dengan menggunakan keywords arguments
def guru(nama, pelajaran):
    print('guru ini bernama', nama)
    print('mengajar', pelajaran)

guru(nama='otong',pelajaran='olahraga')
guru(pelajaran='matematika', nama='entong')
guru('agama', 'mario')


# fungsi dengan menggunakan default arguments
def penjagaSekolah(nama,shift='siang',galak='tidak'):
    print('penjaga sekoah ini bernama:', nama)
    print('shiftnya:', shift)
    print('galak?',galak)

penjagaSekolah('entis')
penjagaSekolah('maman','malam','iya')
penjagaSekolah('asep',galak='sangar')
# penjagaSekolah(shift='malam',galak='iya')       # ini bakal error
