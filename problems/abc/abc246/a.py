from collections import Counter

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

cntx = Counter([x1, x2, x3])
cnty = Counter([y1, y2, y3])
ans = [-1, -1]
for k, v in cntx.items():
    if v == 1:
        ans[0] = k
for k, v in cnty.items():
    if v == 1:
        ans[1] = k
print(*ans)
