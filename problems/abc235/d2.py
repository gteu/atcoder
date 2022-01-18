import sys
sys.setrecursionlimit(200001)

a, n = map(int, input().split())

c = 0
d = {}

def search(n):
    if d.get(n):
        return d.get(n)
    if n == 1:
        return 0
    if n < 10:
        c = 0
        while n % a == 0:
            n //= a
            c += 1
        if n == 1:
            d[n] == c
            return c
        else:
            d[n] == -10**9
            return -10**9

    q = []
    if n % a == 0:
        q.append(n//a)
    q.append(int(str(n)[1:] + str(n)[0]))
    while q:
        search(q.pop())
    
ans = search(n)
if ans < 0:
    print(-1)
else:
    print(ans)
