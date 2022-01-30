from collections import deque
import heapq

N, M = map(int, input().split())
H = list(map(int, input().split()))
to = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    to[u].add(v)
    to[v].add(u)

q = deque([(0, 0)])

INF = 10**9
ans = [-INF] * N
ans[0] = 0
while q:
    cur, s = q.popleft()
    ans[cur] = max(ans[cur], s)
    for nxt in to[cur]:
        if H[cur] > H[nxt]:
            q.append((nxt, s + H[cur] - H[nxt]))
        else:
            q.append((nxt, s + 2 * H[cur] - 2 * H[nxt]))
print(max(ans))