from itertools import product

N, X = map(int, input().split())
L = []
for i in range(N):
    line = list(map(int, input().split()))
    L.append(line[1:])

ans = 0
for A in product(*L):
    v = 1
    for a in A:
        v *= a
    if v == X:
        ans += 1

print(ans)
