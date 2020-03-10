n, m, l = map(int,input().split())
a = list()
b = list()

for i in range(n):
    a_col = list(map(int,input().split()))
    a.append(a_col)
for i in range(m):
    b_col = list(map(int,input().split()))
    b.append(b_col)

# 計算
c = list()
for a_line in a:
    c_line = [0 for num in range(l)]
    for i in range(m):
        for j in range(l):
            c_line[j] += a_line[i] * b[i][j]
# c.append(c_line)
    c_line = [str(c_num) for c_num in c_line]
    print(' '.join(c_line))
