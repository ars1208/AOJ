n = int(input())
a = list(map(int,input().split()))
a = sorted(a)

min = a[0]
max = a[-1]
sum = 0
for i in a:
    sum += i

print(min, max, sum)
