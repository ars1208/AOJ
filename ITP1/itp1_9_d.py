s = input()
q = int(input())
order_list = list()
for i in range(q):
    order = list(map(str,input().split()))
    order_list.append(order)

for order in order_list:
    a = int(order[1])
    b = int(order[2])
    if order[0] == "print":
        print(s[a:b+1])
    elif order[0] == "reverse":
        s_rv = s[a:b+1]
        s_rv = s_rv[::-1]
        s = s.replace(s[a:b+1], s_rv)
    elif order[0] == "replace":
        s_part = s[a:b+1]
        s_part = s_part.replace(s[a:b+1], order[3])
        s = s[:a] + s_part + s[b+1:]
