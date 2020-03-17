s = input()
p = input()

for i in range(len(s)):
    if p in s:
        print("Yes")
        break
    s = s[-1] + s
    s = s[:-1]
else:
    print("No")
