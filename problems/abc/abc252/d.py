from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
ans = N * (N - 1) * (N - 2) // 6
for k, v in cnt.items():
    if v >= 2:
        ans -= (N - v) * v * (v - 1) // 2
    if v >= 3:
        ans -= v * (v - 1) * (v - 2) // 6
print(ans)
