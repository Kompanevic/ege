from itertools import product
alphabet = '0123456'
f=[]
for i in product(alphabet, repeat=4):
    if i[0] > i[1] > i[2] > i[3]:
        f.append(i)
print(len(f))