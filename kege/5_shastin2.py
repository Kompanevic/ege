for n in range(0, 200):
    s = bin(n)[2:]
    if n % 4 == 0:
        s = s + s[-2:]
    else:
        s1 = n % 4
        s = s + bin(s1)[2:]
    r = int(s, 2)
    if r > 250:
        print(r)
