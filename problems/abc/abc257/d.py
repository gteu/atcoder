import sys
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    x, y, p = map(int, input().split())
    A.append((x, y, p))

INF = 10 ** 10
D = [[INF] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            D[i][j] = 0
        else:
            x1, y1, p1 = A[i]
            x2, y2, p2 = A[j]
            D[i][j] = (abs(x1 - x2) + abs(y1 - y2) - 1) // p1 + 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == k or j == k or i == j:
                continue
            D[i][j] = min(max(D[i][k], D[k][j]), D[i][j])

ans = 10 ** 10
for i in range(N):
    tmp = 0
    for j in range(N):
        if i != j:
            tmp = max(tmp, D[i][j])
    ans = min(ans, tmp)
print(ans)
