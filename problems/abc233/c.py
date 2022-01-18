from collections import Counter, defaultdict

N, X = map(int, input().split())
d = defaultdict(int)
d[X] = 1
for i in range(N):
    line = list(map(int, input().split()))
    L, a = line[0], line[1:]
    c = Counter(a)
    newd = defaultdict(int)
    for kc, vc in c.items():
        for kd, vd in d.items():
            if kd % kc == 0:
                newd[kd//kc] += vc * vd
    d = newd

print(d[1])
