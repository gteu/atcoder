import math

n, l, w = map(int, input().split())
A = [0] + list(map(int, input().split())) + [l]

ans = 0
for i in range(1, n + 2):
    if i == 1:
        v = (A[i] - A[i-1] - 1) // w + 1
    else:
        v = (A[i] - A[i-1] - w - 1) // w + 1
    if v >= 0:
        ans += v 

print(ans)