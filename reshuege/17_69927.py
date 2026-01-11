f = open("123")
numbers = list(map(int, f.read().split()))
f.close()
kol = 0
cnt = 0
otvet = []
for num in numbers:
    if num % 32 == 0:
        kol += 1
for i in range(len(numbers) -1):
    a = numbers[i]
    b = numbers[i+1]
    if numbers[i] < 0 or numbers[i+1] < 0:
        if (a + b) < kol:
            cnt += 1
            otvet.append(a + b)
print( cnt,max(otvet))




