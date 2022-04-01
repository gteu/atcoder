from collections import defaultdict

N = int(input())
d = defaultdict(int)
for _ in range(N):
    S = input()
    num = 0
    for s in S:
        num += 10 ** (ord(s) - ord('a'))
    d[num] += 1
ans = 0
for k, v in d.items():
    if v > 1:
        ans += v * (v - 1) // 2
print(ans)
