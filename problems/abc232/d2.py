H, W = map(int, input().split())
C = []
INF = 10 ** 18
for i in range(H):
    C.append(input())
d = [[INF] * W for _ in range(H)]
d[0][0] = 1

stack = [(0, 0)]
ans = -1
while stack:
    i, j = stack.pop()
    ans = max(d[i][j], ans)
    if i + 1 < H and C[i+1][j] == "." and d[i+1][j] == INF:
        d[i+1][j] = d[i][j] + 1
        stack.append((i+1, j))
    if j + 1 < W and C[i][j+1] == "." and d[i][j+1] == INF:
        d[i][j+1] = d[i][j] + 1
        stack.append((i, j+1))
print(ans)