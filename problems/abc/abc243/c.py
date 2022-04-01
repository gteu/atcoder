from collections import defaultdict

N = int(input())
d = defaultdict(list)
xy = []
for i in range(N):
    xy.append(tuple(map(int, input().split())))
S = input()

for i, (x, y) in enumerate(xy):
    d[y].append((x, S[i]))

for k, v in d.items():
    l = 10 ** 9 + 1
    r = - 1
    for x, di in v:
        if di == 'R':
            l = min(l, x)
        else:
            r = max(r, x)
        if l < r:
            print('Yes')
            exit()
print('No')
