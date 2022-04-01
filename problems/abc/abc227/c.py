import math

n = int(input())
err = 0.00000000001

ans = 0
for i in range(1, math.floor(n ** (1/3) + err) + 1):
    for j in range(i, math.floor((n / i) ** (1/2) + err) + 1):
        ans += math.floor(n / i / j + err) - j + 1
print(ans)
