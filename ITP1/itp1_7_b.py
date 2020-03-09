data_list = list()
while True:
    data = list(map(int,input().split()))
    if data == [0,0]:
        break
    data_list.append(data)

for data in data_list:
    cnt = 0
    for a in range(1,data[0]):
        for b in range(a+1,data[0]):
            c = data[1] - a - b
            if c > 0 and c != a and c != b and c > b and c < data[0]+1:
                cnt += 1
    print(cnt)
