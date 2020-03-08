n,m = map(int,input().split())
a = list()
b = list()
for i in range(n):
    a_i = list(map(int,input().split()))
    a.append(a_i)
for i in range(m):
    b.append(int(input()))

for i in range(n):
    sum = 0
    for j in range(m):
        sum += a[i][j] * b[j]
    print(sum)
