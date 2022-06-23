N, M = map(int, input().split())
edges = [[False] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    edges[x - 1][y - 1] = True

ans = 0
for i in range(2 ** N):
    nodes = []
    for j in range(N):
        if i >> j & 1:
            nodes.append(j)
    flg = True
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if not edges[nodes[i]][nodes[j]]:
                flg = False
    if flg:
        ans = max(ans, len(nodes))
print(ans)
