'''
Rjの最小値を保持することで最大利益の更新判定をn回で終わらせる
O(n)のアルゴリズム
'''

n = int(input())
r = list()
for i in range(n):
    r.append(int(input()))

minv = r[0]
maxv = r[1] - r[0]
for j in range(1,n-1):
    maxv = max(maxv, r[j]-minv)
    minv = min(minv, r[j])

print(maxv)
