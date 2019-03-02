# if basic
nilai = 75
if nilai == 75:
    print("nilai anda: ", nilai)

if nilai == 80:
    print("nilai anda: ", nilai)


# nesting if
nilai1 = 75
nilai2 = 80
if nilai1== 75:
    print("nilai anda: ", nilai1)
    if nilai2 == 80:
        print("nilai anda: ", nilai2)


# if in english
nilai3 = 50
if nilai3 == 75: # euqual eksplisit
    print("nilai anda: ", nilai3)

if nilai3 is 60: # equal
    print("nilai anda: ", nilai3)

if nilai3 is not 60: # equal
    print("nilai anda bukan: ", nilai3)


# elif
nilai = 60
if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah D")
else:
    print("ga lulus nih")


# operator logika untuk list dan string
print("\noperator logika untuk list dan string")
gorengan = ["bakwan", "cireng", "bala-bala", "gehu", "combro", "pisang goreng", "pukis", "risoles"]
beli = "bandros"

if beli in gorengan:
    print('Mamang bilang, "ya saya jual', beli, '"')

if not beli in gorengan:
    print('"saya ga jual ', beli, '"')

karakter = "z"
if karakter in beli:
    print("ada ", karakter, "di ", beli)
else:
    print("tidak ada", karakter, "di ", beli)
