import math

n = int(input())
root = math.floor(math.sqrt(n))
ans = 0
d = []
for i in range(1, root + 1):
    d.append((i, n // i))
    ans += n // i
cur = root 
for i, v in d[::-1]:
    ans += i * (v - cur)
    cur = v
print(ans)