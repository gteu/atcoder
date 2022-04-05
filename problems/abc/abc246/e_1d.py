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

q = deque([(ax, ay)])
d = [5 * 10 ** 6] * (N ** 2)
d[ax * N + ay] = 0
while q:
    x, y = q.popleft()
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        for i in range(1, N):
            nx = x + dx * i
            ny = y + dy * i
            if 0 <= nx < N and 0 <= ny < N:
                if nx == bx and ny == by:
                    print(d[(x * N + y)] + 1)
                    exit()
                if S[nx][ny] == '#' or d[nx * N + ny] < d[x * N + y] + 1:
                    break
                if d[nx * N + ny] > d[x * N + y] + 1:
                    d[nx * N + ny] = d[x * N + y] + 1
                    q.append((nx, ny))
            else:
                break

print(-1)
