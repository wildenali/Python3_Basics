list = [1,2,3,4]
tuple = (1,2,3,4)
set = {1,2,3,4}

print(type(list))
print(type(tuple))
print(type(set))



# Dictionary yaitu structur data yang menggunakan mapping
# member1 = {key:value, key:value}
member1 = {"ID":101,
           "Nama":"wilden ali",
           "Status Member":"gold",
           }

print(member1)
print(member1["ID"])
print(member1["Nama"])
print(member1["Status Member"])

print(member1.keys())
print(member1.values())
print(member1.items())

member2 = {"ID":102,
           "Nama":"ucup suracup",
           "Status Member":"silver",
           }

memberlist = {101:member1, 102:member2}
print(memberlist[101])
