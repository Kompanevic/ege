import itertools
alphabet = "ЖИРАФ"
f = itertools.product(alphabet, repeat=4) #Размещение с повторением
s = []
for i in f:
    s.append(list(i))
kol = 0
for x in s:
    if x.count('Р') == 1:
        kol += 1
print(kol)