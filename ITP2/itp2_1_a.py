q = int(input())
data_list = list()
for i in range(q):
    data = input()
    data_list.append(data)

a = list()
for data in data_list:
    if data[0] == "0":
        a.append(data.split()[1])
    elif data[0] == "1":
        print(a[int(data.split()[1])])
    else:
        a.pop(-1)
