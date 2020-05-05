'''
挿入ソート
　入力データの並びが、計算量に大きく影響する
　ある程度整列されたデータには高速に動作する
　安定なソート
'''

n = int(input())
a = list(map(int,input().split()))

print(' '.join(map(str,a)))
for i in range(1,n):
    v = a[i]
    j = i - 1
    while j >= 0 and a[j] > v:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = v
    ans = ' '.join(map(str,a))
    print(ans)
