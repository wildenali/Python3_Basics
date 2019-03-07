# class
# class harus di atas, karena python itu interpreted language, makanya harus berurutan
class mahasiswa():
    nama = 'nama'   # atribut, nilai yang nempel di dalam kelas

    # membuat sebuah method
    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self):
        print(self.nama, 'tidur di kelas')


# main program

otong = mahasiswa()
ucup = mahasiswa()

print(otong)
print(ucup)

print()

otong.nama = "otong surotong"
ucup.nama = "ucup suracup"
print(otong.nama)
print(ucup.nama)

print()

otong.belajar('dengan giat')
ucup.tidur()
