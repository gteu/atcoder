from operator import itemgetter


N, D = map(int, input().split())
walls = []
for i in range(N):
    walls.append(tuple(map(int, input().split())))
walls.sort(key=lambda x: x[1])

pre = None
ans = 0
for L, R in walls:
    if pre and L <= pre + D - 1:
        continue
    else:
        pre = R
        ans += 1
print(ans)