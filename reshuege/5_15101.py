for s in range(1000,10000):
    s1 = str(s)
    k1 = int(s1[0]) + int(s1[1])
    k2 = int(s1[1]) + int(s1[2])
    k3 = int(s1[2]) + int(s1[3])
    f = sorted([k1, k2, k3])
    f1 = str(f[1]) + str(f[2])
    print(f1)


