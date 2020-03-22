def shuffle(m,x):
    tmp = m[:x]
    m = m[x:]
    m = m + tmp
    return m

data_list = list()
while True:
    data = list()
    n = input()
    if n == "-":
        break

    data.append(n)
    m = int(input())
    data.append(m)
    h_list = list()
    for i in range(m):
        h = int(input())
        h_list.append(h)
    data.append(h_list)
    data_list.append(data)

for data in data_list:
    ans = data[0]
    for h in data[2]:
        ans = shuffle(ans,h)
    print(ans)
