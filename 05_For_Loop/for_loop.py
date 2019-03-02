# list sebagai iterables
gorengan = ["bakwan", "cireng", "bala-bala", "gehu", "combro", "pisang goreng", "pukis", "risoles", "tahu isi", "tempe goreng"]

for g in gorengan:
    print(g)
    print(len(g))

# string sebagai iterable
bakwan = 'bakwan'
for i in bakwan:
    print(i)

# for di dalam for
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat']

Daftar_belanja = [gorengan, buah, sayur]
print(Daftar_belanja)
print("\n")
for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)
