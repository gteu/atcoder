from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
cul = 0
d[cul] = 1
ans = 0
for a in A:
    cul += a
    ans += d[cul-K]
    d[cul] += 1
print(ans)