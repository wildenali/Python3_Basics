#usr/bin/python3

text1 = "ini adalah teks"
text2 = "ini hari jum'at"
text3 = 'ini hari jum\'at'
text4 = 'otong berkata, "dimana hey"'
text5 = "otong berkata, \"dimana hey\""
text6 = """
otong berkata, \"dimana hey\"
entong menjawab, 'disini...........'
"""

text7 = r'C:\iniFolder'     # raw string
text8 = "wk"
text9 = "pisang goreng"
t9_0 = text9[4]
t9_1 = text9[0:4]
t9_2 = text9[2:]

print(text1)
# ini adalah teks

print(text2)
# ini hari jum'at

print(text3)
# ini hari jum'at

print(text4)
# otong berkata, "dimana hey"

print(text5)
# otong berkata, "dimana hey"

print(text6)
# otong berkata, "dimana hey"
# entong menjawab, 'disini...........'

print(text7)
# C:\iniFolder

print(10*text8)
# wkwkwkwkwkwkwkwkwkwk

print('kue' 'pukis')
# kuepukis

print(text1 + text2)
# ini adalah teksini hari jum'at

print(t9_0)
# n

print(t9_1)
# pisa

print(t9_2)
# sang goreng