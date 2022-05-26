W, N = map(int, input().split())
x = set()
querys = []
for _ in range(N):
    L, R = map(int, input().split())
    querys.append((L, R))
    x.add(L)
    x.add(R)

x = sorted(x)
x2i = {x: i for i, x in enumerate(x)}
B = [0] * len(x)

ans = []
for L, R in querys:
    li = x2i[L]
    ri = x2i[R]
    m = max(B[li:ri + 1])
    ans.append(m + 1)
    for i in range(li, ri + 1):
        B[i] = m + 1
print(*ans, sep='\n')
