a = list(input().split())
stack = list()

num = 0
for i in a:
    if i.isdigit():
        stack.append(i)
        num += 1
        continue
    elif i == '+':
        ans = int(stack[num-2]) + int(stack[num-1])
    elif i == '-':
        ans = int(stack[num-2]) - int(stack[num-1])
    elif i == '*':
        ans = int(stack[num-2]) * int(stack[num-1])
    elif i == '/':
        ans = int(stack[num-2]) / int(stack[num-1])
    stack.pop()
    stack.pop()
    stack.append(ans)
    num -= 1

print(stack[0])
