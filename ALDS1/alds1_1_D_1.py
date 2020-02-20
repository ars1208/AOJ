'''
素朴なアルゴリズム
for j が 1 から n-1 まで
    for i が 0 から j-1 まで
        
'''

r = []

n = int(input())
for i in range(n):
    i = int(input())
    r.append(i)

maxv = r[1] - r[0]

for j in range(1,n):
    for i in range(j):
        maxv = max(maxv, r[j]-r[i])

print(maxv)
