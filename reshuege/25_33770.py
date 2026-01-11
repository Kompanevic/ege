for i in range(106000000, 107000000 + 1):
    x = set()
    if i % 2 == 0:
        x.add(i)
    else:
        continue
    for j in range(2 if i % 2 == 0 else 3, int(i**0.5) + 1, 1 if i % 2 == 0 else 2):
        if i % j == 0:
            if j % 2 == 0:
                x.add(j)
            if (i // j) % 2 == 0:
                x.add(i // j)
            if len(x) > 3:
                break
    if len(x) == 3:
       print(i)