from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
ax -= 1
ay -= 1
bx -= 1
by -= 1
S = []
for _ in range(N):
    S.append(input())
if (ax + ay) % 2 != (bx + by) % 2:
    print(-1)
    exit()

q = deque([(ax, ay, -1)])
d = [[[10 ** 9] * 4 for _ in range(N)] for _ in range(N)]
dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
for i in range(4):
    d[ax][ay][i] = 0
while q:
    x, y, i = q.popleft()
    for j in range(4):
        nx = x + dirs[j][0]
        ny = y + dirs[j][1]
        if 0 <= nx < N and 0 <= ny < N and S[nx][ny] == '.':
            if i == j:
                if d[nx][ny][i] > d[x][y][i]:
                    d[nx][ny][i] = d[x][y][i]
                    q.appendleft((nx, ny, i))
            else:
                if d[nx][ny][j] > d[x][y][i] + 1:
                    d[nx][ny][j] = d[x][y][i] + 1
                    q.append((nx, ny, j))

if min(d[bx][by]) < 10 ** 9:
    print(min(d[bx][by]))
else:
    print(-1)
