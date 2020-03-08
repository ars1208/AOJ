# 直接的な実装

n = int(input())
data_list = list()
for i in range(n):
    data = list(map(int,input().split()))
    data_list.append(data)

apart = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],'####################',[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],'####################',[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],'####################',[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

for data in data_list:
    apart[((data[0]-1)*4)+(data[1]-1)][data[2]-1] = apart[((data[0]-1)*4)+(data[1]-1)][data[2]-1] + data[3]

for ridge in apart:
    if str(ridge[0]).isdigit():
        ridge = [str(i) for i in ridge]
        print('',' '.join(ridge))
    else:
        print(ridge)
