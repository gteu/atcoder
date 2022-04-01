from collections import deque
from dis import dis

MOD = 10 ** 9 + 7
N, M = map(int, input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

INF = 10 ** 9
q = deque([0])
dist = [INF] * N
ways = [0] * N
dist[0] = 0
ways[0] = 1

while q:
    cur = q.popleft()
    for nxt in to[cur]:
        if dist[nxt] == INF:
            q.append(nxt)
            dist[nxt] = dist[cur] + 1
            ways[nxt] += ways[cur]
        elif dist[nxt] == dist[cur] + 1:
            ways[nxt] += ways[cur]
print(ways[N - 1] % MOD)
