from collections import defaultdict

N, C = map(int, input().split())
D = defaultdict(int)
for _ in range(N):
    a, b, c = map(int, input().split())
    D[a] += c
    D[b + 1] -= c

D = sorted(D.items())
ans = 0
pre = 0
price = 0
for cur, d in D:
    ans += min(C, price) * (cur - pre)
    pre = cur
    price += d
print(ans)
