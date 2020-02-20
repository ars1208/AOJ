import copy

n = int(input())
a = list(map(str,input().split()))
a_b = copy.deepcopy(a)
a_s = copy.deepcopy(a)

# バブルソート
def bubble(a_b, n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if int(a_b[j][1]) < int(a_b[j-1][1]):
                tmp = a_b[j]
                a_b[j] = a_b[j-1]
                a_b[j-1] = tmp
    return a_b

# 選択ソート
def selection(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(a[j][1]) < int(a[minj][1]):
                minj = j
        tmp = a[i]
        a[i] = a[minj]
        a[minj] = tmp
    return a

# 安定性判定
def stable(in_a, out_a, n):
    for i in range(n):
        for j in range(i+1, n):
            for a in range(n):
                for b in range(a+1,n):
                    if in_a[i][1] == in_a[j][1] and in_a[i] == out_a[b] and in_a[j] == out_a[a]:
                        return "Not stable"
    return "Stable"


print(' '.join(bubble(a_b,n)))
print(stable(a, bubble(a_b,n), n))
print(' '.join(selection(a_s,n)))
print(stable(a, selection(a_s,n), n))
