from collections import defaultdict
from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
d = defaultdict(list)

for i, a in enumerate(A):
    d[a].append(i + 1)

ans = []
for _ in range(Q):
    L, R, X = map(int, input().split())
    ans.append(bisect_right(d[X], R) - bisect_left(d[X], L))
print(*ans, sep='\n')
