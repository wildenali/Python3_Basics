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
print(text2)
print(text3)
print(text4)
print(text5)
print(text6)
print(text7)
print(100*text8)
print('kue' 'pukis')
print(text1 + text2)

# Slice itu motong kata
print(t9_0)
print(t9_1)
print(t9_2)
