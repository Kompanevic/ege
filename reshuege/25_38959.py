i = 200000000
kol = 0
while kol < 5:
    i += 1
    x = set()
    x.add(i)
    for j in range(2 if i % 2 == 0 else 3, int(i**0.5) + 1, 1 if i % 2 == 0 else 2):
        if i % j == 0:
            x.add(j)
            x.add(i // j)
    if len(x) < 5:
        continue
    f = sorted(list(x))
    q = (f[0]) * (f[1]) * (f[2]) * (f[3]) * f[4]
    if 0 < q < i:
        kol += 1
        print(q)