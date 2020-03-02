n = int(input())
ans_list = list()

for i in range(1,n+1):
    if i % 3 == 0:
        ans_list.append(str(i))
    elif i % 10 == 3:
        ans_list.append(str(i))
    elif '3' in str(i):
        ans_list.append(str(i))

print('', ' '.join(ans_list))
