from collections import deque

N, M = map(int, input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    to[u].append(v)
    to[v].append(u)

short = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            q = deque()
            q.append((i))
            visited = [False] * N
            visited[i] = True
            prev = [-1] * N
            while q:
                cur = q.popleft()
                for nxt in to[cur]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        prev[nxt] = cur
                        q.append(nxt)
            path = [j]
            while path[-1] != -1:
                path.append(prev[path[-1]])
            path = path[::-1][1:]
            short[i][j] = path

print(short)
ans = 0
# for i in range(2 ** N):
#     for j in range(N):
#         if i >> j & 1:
