from collections import deque
import sys
input = sys.stdin.readline
H, W = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch -= 1
cw -= 1
dh -= 1
dw -= 1
S = []
for _ in range(H):
    S.append(input())

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
INF = 10 ** 9
d = [[INF] * W for _ in range(H)]
q = deque([(ch, cw)])
d[ch][cw] = 0
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.':
            if d[nx][ny] > d[x][y]:
                d[nx][ny] = d[x][y]
                q.appendleft((nx, ny))

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.':
                if d[nx][ny] > d[x][y] + 1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))

if d[dh][dw] == INF:
    print(-1)
else:
    print(d[dh][dw])
