cnt_al = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

word_list = list()
while True:
    words = input().lower()
    word_list.append(words)

for words in word_list:
    for word in words:
        if word == "":
            continue
        if word in cnt_al:
            cnt_al[word] += 1

for al,cnt in cnt_al.items():
    print(al,':',cnt)
