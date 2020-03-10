r, c = map(int,input().split())

table = list()
for i in range(r):
    line = list(map(int,input().split()))
    table.append(line)

col_sum_list = [0 for i in range(len(table[0]))]
for line in table:
    line_sum = 0
    for i in range(len(line)):
        line_sum += line[i]
        col_sum_list[i] += line[i]
    line.append(line_sum)
col_sum_list.append(sum(col_sum_list))

for line in table:
    line = [str(i) for i in line]
    print(' '.join(line))

col_sum_list = [str(i) for i in col_sum_list]
print(' '.join(col_sum_list))
