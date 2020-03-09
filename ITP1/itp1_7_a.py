test_list = list()
while True:
    test = list(map(int,input().split()))
    if test == [-1,-1,-1]:
        break
    test_list.append(test)

for test in test_list:
    m = test[0]
    f = test[1]
    r = test[2]
    if m == -1 or f == -1:
        print('F')
    elif m + f >= 80:
        print('A')
    elif m + f >= 65 and m + f < 80:
        print('B')
    elif m + f >= 50 and m + f < 65:
        print('C')
    elif m + f >= 30 and m + f < 50:
        if r >= 50:
            print('C')
        else:
            print('D')
    elif m + f < 30:
        print('F')
