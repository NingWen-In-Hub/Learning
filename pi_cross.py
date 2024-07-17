input_line = input()
n = int(input_line)
W = 5

line = []
for i in range(n):
    line.append(input())

def if_del_able(line, n, x, y):
    _self = line[x][y]
    ref = True
    if _self == ".":
        return False
    if x-1 >= 0:
        ref = ref and (_self == line[x-1][y])
    if x+1 < n:
        ref = ref and (_self == line[x+1][y])
    if y-1 >= 0:
        ref = ref and (_self == line[x][y-1])
    if y+1 < W:
        ref = ref and (_self == line[x][y+1])
    return ref

def do_del(line, n, del_list):
    for p in del_list:
        if p[0]-1 >= 0:
            line[p[0]-1] = line[p[0]-1][:p[1]] + "." + line[p[0]-1][p[1]+1:]
        if p[0]+1 < n:
            line[p[0]+1] = line[p[0]+1][:p[1]] + "." + line[p[0]+1][p[1]+1:]
        if p[1]-1 >= 0:
            line[p[0]] = line[p[0]][:p[1]-1] + "." + line[p[0]][p[1]:]
        if p[1]+1 < W:
            line[p[0]] = line[p[0]][:p[1]+1] + "." + line[p[0]][p[1]+2:]
        line[p[0]] = line[p[0]][:p[1]] + "." + line[p[0]][p[1]+1:]
    return line

def ph_delete(line, n):
    wait_for_del = []
    ref = False
    # d = 0
    for r in range(n):
        for l in range(W):
            if if_del_able(line, n, r, l):
                ref = True
                wait_for_del.append([r,l])
                # d = line[r][l]
    
    # print(wait_for_del)
    line = do_del(line, n, wait_for_del)

    # do fill
    for r in range(n-1, -1, -1):
        for l in range(W):
            if line[r][l] == ".":
                for t in range(r-1, -1, -1):
                    if line[t][l] != ".":
                        line[r] = line[r][:l] + line[t][l] + line[r][l+1:]
                        line[t] = line[t][:l] + "." + line[t][l+1:]
                        break
    return(ref)

r = ph_delete(line, n)
while(r):
    r = ph_delete(line, n)


for i in line:
    print(i)
