H, W = map(int, input().split())
C = []
INF = 10 ** 18
for i in range(H):
    C.append(input())
d = [[-INF] * W for _ in range(H)]
d[0][0] = 1

ans = 0
for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            continue
        if i != 0:
            d[i][j] = max(d[i][j], d[i-1][j] + 1)
        if j != 0:
            d[i][j] = max(d[i][j], d[i][j-1] + 1)
        ans = max(ans, d[i][j])
print(ans)