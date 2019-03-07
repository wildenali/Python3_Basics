# class
# class harus di atas, karena python itu interpreted language, makanya harus berurutan
class mahasiswa():

    # nilai = 5     # global attribute
    __nilai = 5     # private attribute, ciri ciri private ada __xxx (undesocre nya dua kali)

    jurusan = "teknik tata boga"

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim    # public

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def cek_status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama,'lulus')



# main program

otong = mahasiswa("otong belangbetong", 10001)
ucup = mahasiswa("mikael ucup", 10002)

otong.uts(10)
otong.uas(50)
otong.cek_status()

print()

ucup.uts(10)
ucup.uas(25)
ucup.cek_status()

print(otong.__nilai)
