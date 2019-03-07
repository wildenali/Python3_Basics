#
class mahasiswa():

    jurusan = "ekonomi"

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim    # public





# main program

otong = mahasiswa("otong belangbetong", 10001)
ucup = mahasiswa("mikael ucup", 10002)

# mahasiswa.jurusan = "ekonomi mikro"
otong.jurusan = "ekonomi mikro"     # membuat variable instances (sesuatu)
otong.kegemaran = "menari"

print(mahasiswa.jurusan)
print(otong.jurusan)
print(otong.kegemaran)
print(ucup.jurusan)

print(mahasiswa.__dict__)
print(otong.__dict__)
print(ucup.__dict__)
