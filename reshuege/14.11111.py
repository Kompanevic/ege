def f(x):
    s = ''
    while x != 0:
        s = str(x % 4) + s
        x = x // 4
    return s
q = []
for s in range(200,0,-1):
    if f(s)[-3:] == '123':
        q.append(s)
print(q)