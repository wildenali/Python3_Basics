class Ojek(object):
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ndaerah:',self.daerah)

# ini kelas turunan dari class Ojek
class Gojek(Ojek):
    pass

    # atau

    # def cek_id_abang(self):
    #     print('cek aplikasi gojek')


ojek1 = Ojek('mario','manual','bandung selatan')
ojek2 = Ojek('jakson','matic','tasikmalaya')
ojek3 = Gojek('ucup','semi matic','garut')

ojek1.cek_id_abang()
print()
ojek2.cek_id_abang()
print()
ojek3.cek_id_abang()
