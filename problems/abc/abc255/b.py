import math

N, K = map(int, input().split())
A = set(map(lambda x: int(x) - 1, input().split()))
points = []
for i in range(N):
    X, Y = map(int, input().split())
    points.append((X, Y))

ans = 0
for i in range(N):
    if i in A:
        continue
    tmp = 10 ** 10
    for j in range(N):
        if i not in A and j in A:
            x1, y1 = points[i]
            x2, y2 = points[j]
            tmp = min(tmp, math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
    ans = max(ans, tmp)

print(ans)
