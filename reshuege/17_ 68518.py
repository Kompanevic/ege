f = open("123")
numbers = list(map(int, f.read().split()))
f.close()
kol = 0
cnt = 0
mine = min(x for x in numbers if x % 19 == 0)
sume = []
for i in range(len(numbers)-1):
    a = numbers[i]
    b = numbers[i+1]
    if a % mine == 0 or b % mine == 0:
        cnt += 1
        sume.append(a+b)
print(cnt, max(sume))







