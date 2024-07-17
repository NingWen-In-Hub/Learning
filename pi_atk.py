_t = input().split(' ')
A = int(_t[0])
B = int(_t[1])

n = int(input())
hps_str = input().split(' ')
hps = []
for h in hps_str:
    hps.append(int(h))

re_num = 0
while n > 0:
    re_num += 1
    if B * n > min(max(hps), A):
        for i in range(len(hps)):
            hps[i] -= B
    else:
        hps.sort()
        hps[-1] -= A
    
    _hps = [i for i in hps if i > 0]
    hps = _hps
    n = len(hps)

print(re_num)
