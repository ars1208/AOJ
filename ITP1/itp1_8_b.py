x_list = list()
while True:
    x = str(input())
    if x == '0':
        break
    x_list.append(x)

for x in x_list:
    sum = 0
    for num in x:
        sum += int(num)
    print(sum)
