'''
選択ソート
　離れた場所を交換することがあるため安定なソートではない
　O(N^2)のアルゴリズム
'''

n = int(input())
a = list(map(int,input().split()))

cnt = 0
for i in range(n):
    minj = i
    for j in range(i,n):
        if a[j] < a[minj]:
            minj = j
    if a[i] != a[minj]:
        cnt += 1
    tmp = a[i]
    a[i] = a[minj]
    a[minj] = tmp

print(' '.join(map(str,a)))
print(cnt)
