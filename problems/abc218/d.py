from collections import defaultdict

N = int(input())
x_d = defaultdict(list)
y_d = defaultdict(list)
dots = []
for _ in range(N):
    x, y = map(int, input().split())
    x_d[x].append(y)
    y_d[y].append(x)
    dots.append((x, y))

ans = 0
for x1, y1 in dots:
    for y2 in x_d[x1]:
        for x2 in y_d[y1]:
            if x2 > x1 and y2 > y1 and y2 in x_d[x2]:
                ans += 1

print(ans)