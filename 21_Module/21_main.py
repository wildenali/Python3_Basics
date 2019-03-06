# Cara Pertama ==============================
print("# Cara Pertama ==============================")
import matematika

matematika.tambah(3,4)
matematika.kurang(5,6)

# Cara Kedua ==============================
print('\n# Cara Kedua ==============================')
import matematika as modol

modol.tambah(3,4)
modol.kurang(5,6)

# Cara Ketiga ==============================
print('\n# Cara Ketiga ==============================')
from matematika import tambah, kurang

tambah(3,4)
kurang(5,6)

# Cara Keempat ==============================
print('\n# Cara Keempat ==============================')
from matematika import tambah as t

t(6,5)
