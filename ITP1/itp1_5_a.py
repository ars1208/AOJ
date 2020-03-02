s_list = list()

while True:
    h,w = map(int,input().split())
    s_pair = [h,w]
    if s_pair == [0,0]:
        break
    s_list.append(s_pair)

for pair in s_list:
    for h in range(pair[0]):
        for w in range(pair[1]):
            print('#', end='')
        print('')
    print('')
