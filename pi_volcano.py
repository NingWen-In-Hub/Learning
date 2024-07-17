_t = input().split(' ')
n = int(_t[0])
r = int(_t[1])
d2 = (2*r) ** 2

line = []
group_d = {}

for i in range(n):
    _v = input().split(' ')
    vx = int(_v[0])
    vy = int(_v[1])

    _same_group = []
    for g in group_d:
        for v in group_d[g]:
            if (vx-v[0])**2 + (vy-v[1])**2 <= d2:
                # group_d[g].append([vx, vy])
                _same_group.append(g)
                break
    
    if len(_same_group) == 0:
        # new land
        group_d[i] = [[vx, vy]]
    elif len(_same_group) == 1:
        # in one group
        group_d[_same_group[0]].append([vx, vy])
    else:
        # gather group
        _g = _same_group.pop(0)
        group_d[_g].append([vx, vy])
        for g in _same_group:
            for v in group_d[g]:
                group_d[_g].append(v)
            del group_d[g]

print(len(group_d))

line.sort()
print(group_d)
