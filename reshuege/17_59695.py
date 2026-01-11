otv = []
for n in range (567_891_234, 567_000_000, -1):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '11' +  s
    else:
        s = '1' + s + '10'
    r = int (s,2)
    otv.append(r)
print(max(otv))