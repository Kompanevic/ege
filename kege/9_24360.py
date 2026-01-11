f = open('9')
ans = set()
for line in f.readlines():
    numbers = [int(x) for x in line.split()]
    numbers.sort()
    if numbers[0]**2 in numbers:
        ans.add(sum(numbers))
        continue
    d = {x for x in numbers}
    par = 0
    for x in d:
        par += numbers.count(x) // 2
    if par >= 3:
        ans.add(sum(numbers))
print(min(ans))