from collections import deque

N, Q = map(int, input().split())
to = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)

INF = 10 ** 9
dist = [INF] * N
dist[0] = 0
q = deque([0])
while q:
    cur = q.popleft()
    for nxt in to[cur]:
        if dist[nxt] == INF:
            q.append(nxt)
            dist[nxt] = dist[cur] + 1

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] - dist[d]) % 2:
        print('Road')
    else:
        print('Town')
