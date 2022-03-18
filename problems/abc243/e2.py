import sys

input = sys.stdin.buffer.readline
INF = 10 ** 18
N, M = map(int, input().split())
d = [[INF] * N for _ in range(N)]
edge = []
for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    d[A][B] = C
    d[B][A] = C
    edge.append((A, B, C))

changed = [[False] * N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][j] >= d[i][k] + d[k][j]:
                changed[i][j] = True
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

ans = 0
for a, b, c in edge:
    ans += changed[a][b]
print(ans)
