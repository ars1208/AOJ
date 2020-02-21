i = 1
ans_list = list()

while True:
    x = int(input())
    if x == 0:
        break
    ans_list.append(x)
    i += 1

for i in range(len(ans_list)):
    print("Case " + str(i+1) + ": " + str(ans_list[i]))
