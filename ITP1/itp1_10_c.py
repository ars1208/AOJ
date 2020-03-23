s_list = list()
while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(float,input().split()))
    s_list.append(s)

for s in s_list:
    m = sum(s) / len(s)
    dispersion = 0
    for s_num in s:
        dispersion += (s_num - m)**2
    dispersion /= len(s)
    std = dispersion**0.5
    print(std)
