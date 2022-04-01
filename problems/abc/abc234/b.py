from itertools import combinations
import math

N = int(input())
dots = []
for _ in range(N):
    dots.append(list(map(int, input().split())))

ans = -1
for (x1, y1), (x2, y2) in combinations(dots, 2):
    ans = max(ans, (x2 - x1) ** 2 + (y2 - y1) ** 2)
print(math.sqrt(ans))
