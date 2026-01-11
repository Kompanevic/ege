for a in range(0, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if  (x + 2 * y < a) or (y < x) or (y > 22):
                k += 1
    if k == 90_000:
        print(a)
        break