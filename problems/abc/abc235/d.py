from collections import deque

a, n = map(int, input().split())

q = deque([(n, 0)])
d = set()

ans = 10**9
while q:
    v, c = q.popleft()
    d.add(v)
    if v < 10:
        while v % a == 0:
            v //= a
            c += 1
        if v == 1:
            ans = min(ans, c)
        continue

    if v % a == 0:
        n = v//a
        q.append((n, c+1))
    n = int(str(v)[1:] + str(v)[0])
    if n not in d and str(v)[1] != "0":
        q.append((n, c+1))

if ans == 10**9:
    print(-1)
else:
    print(ans)