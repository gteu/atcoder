import sys
sys.setrecursionlimit(300000)


def dfs(cur):
    visited[cur] = True
    for nxt in to[cur]:
        if not visited[nxt]:
            dfs(nxt)


N, M = map(int, input().split())
to = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)

ans = 0
for i in range(N):
    visited = [False] * N
    dfs(i)
    ans += sum(visited)
print(ans)
