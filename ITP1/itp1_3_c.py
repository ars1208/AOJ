ans_list = list()
while True:
    x,y = map(int,input().split())
    xy = [x,y]
    if [x,y] == [0,0]:
        break
    ans_list.append([x,y])

for pair in ans_list:
    pair =sorted(pair)
    pair = [str(n) for n in pair]
    print(' '.join(pair))
