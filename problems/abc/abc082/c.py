from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)
ans = 0
for k, v in cnt.items():
    if k < v:
        ans += v - k
    elif k > v:
        ans += v
print(ans)
