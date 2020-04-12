from collections import deque

q = int(input())
data_list = list()
for i in range(q):
    data = input()
    data_list.append(data)

a = deque()
for data in data_list:
    if data[0] == "0":
        if data.split()[1] == "1":
            a.append(data.split()[2])
        else:
            x = data.split()[2]
            a.appendleft(x)
        # print(a)
    elif data[0] == "1":
        print(a[int(data.split()[1])])
        # print(a)
    else:
        if data.split()[1] == "1":
            a.pop()
        else:
            a.popleft()
        # print(a)
