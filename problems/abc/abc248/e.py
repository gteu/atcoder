from fractions import Fraction
from collections import defaultdict

N, K = map(int, input().split())

lines_x0 = defaultdict(int)
lines_y = defaultdict(int)
points = []
for _ in range(N):
    X, Y = map(int, input().split())
    points.append((X, Y))

if K == 1:
    print('Infinity')
    exit()

for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        if x1 == x2:
            lines_y[x1] += 1
        else:
            lines_x0[(Fraction(y1 - y2, x1 - x2),
                     Fraction(x1 * y2 - x2 * y1, x1 - x2))] += 1

ans = 0
for k, v in lines_x0.items():
    if v >= K * (K - 1) // 2:
        ans += 1
for k, v in lines_y.items():
    if v >= K * (K - 1) // 2:
        ans += 1
print(ans)
