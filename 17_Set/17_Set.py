# tipe data Set -> Himpunan

# karakteristik Himpunan:
    # 1. Tidak memiliki urutan
    # 2. Dua nama yang sama, di anggap satu data

# set{}
superhero = {"wiro sableng","si buta dari goa hantu","saras 008", "gatot kaca","panji manusia milenium"}
superhero.add("mak lampir")
superhero.add("wiro sableng")
print(superhero)

hewan = set()
hewan.add("ayam")
hewan.add("sapi")
hewan.add("bebek")
hewan.add("kambing")
hewan.add(212)
print(hewan)
#print(sorted(hewan))   # kalau di tambah 212, tidak bisa di sorted

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}
print(ganjil.union(genap))
print(ganjil.intersection(prima))
