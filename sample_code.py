n = int(input())
a = list(map(str,input().split()))

def selection(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(a[j][1]) < int(a[minj][1]):
                minj = j
        tmp = a[i]
        a[i] = a[minj]
        a[minj] = tmp
        print(a)
    return a

print(' '.join(selection(a,n)))
