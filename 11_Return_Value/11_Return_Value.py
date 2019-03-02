print('# fungsi dengan return value')
# fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari',argumen,'adalah',total)
    return total

a = kuadrat(3)
print(a)


# fungsi dengan return value dan multiple argumen
print('\n# fungsi dengan return value dan multiple argumen')
def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total

a = tambah(3,4)
b = kali(3,4)
c = kali(3,a)
d = kali(3,tambah(5,3))
print(a)
print(b)
print(c)
print(d)
