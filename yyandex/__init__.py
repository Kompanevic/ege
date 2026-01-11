for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                if ((w or x or (not z) or y) and (w or x or (not z) or (not y)) and (w or (not x) or (not z) or (not y))) == 0:
                    print(x,y,z,w)

def f(n):
    s=''
    while n > 0:
        s = str(n%3) + s
        n //= 3
    return s
c = []
for n in range(1,1000):
    s = f(n)
    if n % 3 == 0:
        s = '1' + s + '02'
    else:
        s = s + f((n % 3) * 4)
    r = int(s, 3)
    if r < 199:
        c.append(n)
print(max(c))

def f(n):
    s=''
    while n > 0:
        s = str(n%7) + s
        n //= 7
    return s
c = []
for n in range(1,1000):
    s = f(n)
    if s.count('2') % 2 == 0:
        s += '555'
    else:
        s = '1' + s
    r = int(s,7)
    if r < 3799:
        c.append(n)
print(max(c))

def f(n):
    s=''
    while n > 0:
        s = str(n%7) + s
        n //= 7
    return s
c = []
for n in range(1,1000):
    s = f(n)
    if n % 7 == 0:
        s += s[:2]
    else:
        s = s + f((n % 7) * 2)
    r = int(s,7)
    if r < 220:
        c.append(n)
print(max(c))
