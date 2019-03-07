# Cara menggunakan eksternal package
# 1. python sudah terinstal
# 2. koneksi internet
# 3. dependency



# Contoh nya disini akan meng install package numpy (numerical python)

# ================ coba numpy ================
# import numpy as np
#
# # cara menggabungkan list biasa aja
# a = [1,2,3,4]
# b = [5,6,7,8]
# print(a+b)
#
# print()
#
# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# print(a+b)
# ================ coba numpy ================


# ================ coba pillow ================
from PIL import Image

im = Image.open("foto.png")

print("format file: " + im.format)
print("format file: " + str(im.size))
print("format file: " + im.mode)

im.show()
# ================ coba pillow ================
