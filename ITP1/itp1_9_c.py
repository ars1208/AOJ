n = int(input())
pair_list = list()
for i in range(n):
    pair = list(map(str,input().split()))
    pair_list.append(pair)

a = 0
b = 0
for card in pair_list:
    if card[0] == card[1]:
        a += 1
        b += 1
        continue

    if card == sorted(card):
        b += 3
    else:
        a += 3

print(a,b)
