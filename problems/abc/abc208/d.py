INF = 10 ** 9
N, M = map(int, input().split())
d = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d[a][b] = c
for i in range(N):
    d[i][i] = 0

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            if d[i][j] != INF:
                ans += d[i][j]
print(ans)
