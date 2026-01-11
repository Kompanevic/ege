def summa(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return (s)


for n in range(10000):
    p = ''
    for i in range(3):
        if summa(n) % 2 == 0:
            p = bin(n)[2:] + '0'
            n = int(p, 2)
        else:
            p = bin(n)[2:] + '1'
            n = int(p, 2)
    r = int(p, 2)
    if r > 2054:
        print(r)
        break