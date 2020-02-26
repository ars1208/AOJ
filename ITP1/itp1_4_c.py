ans_list = list()

while True:
    a,op,b = map(str,input().split())
    a = int(a)
    b = int(b)
    if op == '?':
        break
    elif op == '+':
        ans_list.append(a+b)
    elif op == '-':
        ans_list.append(a-b)
    elif op == '*':
        ans_list.append(a*b)
    elif op == '/':
        ans_list.append(a//b)

for ans in ans_list:
    print(ans)
