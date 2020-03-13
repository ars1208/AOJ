input_list = list(map(str,input().split(',')))

output_list = list()
for word in input_list:
    word = word.swapcase()
    output_list.append(word)

print(','.join(output_list))
