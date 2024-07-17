input_line = input()
n = int(input_line)

line = {}
re_num = 0
for i in range(n*2):
    k = int(input())
    if k in line.keys():
        # add re number
        re_num += i - line[k]
        del line[k]
    else:
        line[k] = i

print(re_num)
