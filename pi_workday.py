input_line = input()
n = int(input_line)

line = []
for i in range(n):
    _temp = input().split(' ')
    _s_e = []
    for _t in _temp:
        _s_e.append(int(_t))
    line.append(_s_e)

line.sort()
# clean list
n_line = []
s = line[0][0]
e = line[0][1]
for i in range(1, len(line), 1):
    if line[i][0]-1 <= e:
        e = max(e, line[i][1])
    else:
        n_line.append([s, e])
        s = line[i][0]
        e = line[i][1]
n_line.append([s, e])

# print(line)
# print(n_line)

# get longest workday
longest = 0
for workday in n_line:
    longest = max(longest, workday[1] - workday[0] + 1)
print(longest)
