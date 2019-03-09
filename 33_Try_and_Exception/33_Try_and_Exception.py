
# ======================== error runtime ========================
# angka = int(input("masukan angka sembarang?\n"))
# print(angka)


# # ======================== error runtime ========================
# # kalau pembaginya 0, maka apps nya bakal keluar
# def pembagian(a,b):
#     return 1/b
#
# penyebut = int(input("masukan angka penyebut?\n"))
# pembilang = int(input("masukan angka pembilang?\n"))
#
# print(pembagian(penyebut,pembilang))


# ======================== error handling basic ========================
# try:
#     a = 1/0
# except:
#     print("error pembagi nol")
#
# print("akhir program")


# ======================== error handling contoh 1 ========================
# while True:
#     try:
#         angka = int(input("masukan angka: "))
#     except:
#         print("yang anda masukan bukan angka")
#
# print("berhasil, anda memasukan angka: ", angka)


# ======================== error handling contoh 1 ========================
# tangkap error nya (tangkap flagnya)
# """
# kalau
# hasil = 1/0
# maka akan keluar error -> ZeroDivisionError
# """
#
# print("ini adalah program pembagian")
# while True:
#     try:
#         penyebut = int(input("masukan angka penyebut: "))
#         pembilang = int(input("masukan angka pembilang: "))
#         hasil = penyebut/pembilang
#         break
#     except ValueError:
#         print("yang anda masukan bukan angka")
#     except ZeroDivisionError:
#         print("yang anda masukan nol, JANGAN masukan NOL")
#
# print("berhasil, hasil pembagian adalah: ", hasil)


# ======================== error handling contoh 2 ========================
# tangkap error yang lebih UMUM
# print("ini adalah program pembagian")
# while True:
#     try:
#         penyebut = int(input("masukan angka penyebut: "))
#         pembilang = int(input("masukan angka pembilang: "))
#         hasil = penyebut/pembilang
#         break
#     except Exception as err:
#         print(err)
#
# print("berhasil, hasil pembagian adalah: ", hasil)

# ======================== error handling contoh 3 ========================
# tangkap error yang lebih ga ada IMPORT nya (no2 type of error)
print("ini adalah program pembagian")
while True:
    try:
        import panda
        penyebut = int(input("masukan angka penyebut: "))
        pembilang = int(input("masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError:
        print("yang anda masukan bukan angka")
    except ZeroDivisionError:
        print("yang anda masukan nol, JANGAN masukan NOL")
    except ImportError:
        print("ga ada IMPORT nyaaa")

print("berhasil, hasil pembagian adalah: ", hasil)



"""
    type of exception errors
    1. IOError
    2. ImportError
    3. ValueError
    4. Division by zero
    5. KeyboadInterupted
    6. EOFError
"""
