# class
class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim    # public

        mahasiswa.jumlah_mahasiswa += 1





# main program

otong = mahasiswa("otong belangbetong", 10001)
ucup = mahasiswa("mikael ucup", 10002)
cassandra = mahasiswa("cassandra aja", 10003)

print(mahasiswa.jumlah_mahasiswa)
