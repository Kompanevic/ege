for i in range(112500000,112550000):
    x = set()
    for j in range(2 if i % 2 == 0 else 3, int(i**0.5) + 1, 1 if i % 2 == 0 else 2):
        if i % j == 0:
            x.add(j)
            x.add(i // j)
            if len(x) > 2:
                break
    if len(x) < 2:
        continue
    f = sorted(list(x))
    q = int(f[-1]) + (f[-2])
    if q % 10000 == 1214:
        print(i)
