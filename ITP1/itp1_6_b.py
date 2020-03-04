n = int(input())
trump = dict()

for i in range(n):
    mark, num = input().split()
    mark = str(mark)
    num =int(num)
    if mark not in trump:
        trump[mark] = list()
    trump[mark].append(num)

for mark in trump:
    if mark == 'S':
        for i in range(1,14):
            if i not in trump[mark]:
                print(mark, i)

for mark in trump:
    if mark == 'H':
        for i in range(1,14):
            if i not in trump[mark]:
                print(mark, i)

for mark in trump:
    if mark == 'C':
        for i in range(1,14):
            if i not in trump[mark]:
                print(mark, i)

for mark in trump:
    if mark == 'D':
        for i in range(1,14):
            if i not in trump[mark]:
                print(mark, i)
