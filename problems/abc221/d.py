from bisect import bisect_left

n = int(input())
A = []
s = set()
for _ in range(n):
    x, y = map(int, input().split())
    s.add(x)
    s.add(y)
    A.append((x, y))
s = sorted(list(s))

comp_A = []
for x, y in A:
    comp_x = bisect_left(s, x)
    comp_y = bisect_left(s, y)
    comp_A.append((comp_x, comp_y))

login = [0] * len(comp_A)

