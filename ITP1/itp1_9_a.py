w = input()
t_list = list()
while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    t_list.append(t)

cnt = 0
for t in t_list:
    for word in t.split(" "):
        if w.lower() == word.lower():
            cnt += 1

print(cnt)
