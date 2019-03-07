# class
# class harus di atas, karena python itu interpreted language, makanya harus berurutan
class mahasiswa():
    nama = 'nama'   # atribut, nilai yang nempel di dalam kelas

    # membuat init
    # ketika kelas otong = mahasiswa() di panggil, maka si init akan muncul
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

    # membuat sebuah method
    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self):
        print(self.nama, 'tidur di kelas')


# main program

otong = mahasiswa("otong belangbetong", 10001)
print(otong.nama)
print(otong.nim)

otong.nama = "otong ganteng"
print(otong.nama)

# jadi __init__ itu di pakai kalau di pyqt itu kaya QLabel, QPushButton("nama tombol"), QListWidget, dll
