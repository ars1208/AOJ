def minkowski_dist(x, y, n, p):
    d = 0
    for i in range(n):
        d += abs(x[i] - y[i])**p
    d = d**(1/p)
    return d

n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

for p in range(1,4):
    print(minkowski_dist(x,y,n,p))

d = abs(x[0]-y[0])
for i in range(n):
    el = abs(x[i]-y[i])
    d = max(d,el)
print(d)
