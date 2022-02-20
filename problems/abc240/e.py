import sys
sys.setrecursionlimit(300000)
N = int(input())
to = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    to[u].append(v)
    to[v].append(u)

visited = [False] * N
n = 0
ans = [[10 ** 9, -1] for _ in range(N)]


def dfs(cur):
    global n
    visited[cur] = True
    flag = True
    for nxt in to[cur]:
        if not visited[nxt]:
            flag = False
            dfs(nxt)
            ans[cur][0] = min(ans[cur][0], ans[nxt][0])
            ans[cur][1] = max(ans[cur][1], ans[nxt][1])
    if flag:
        n += 1
        ans[cur] = [n, n]


dfs(0)
for x, y in ans:
    print(x, y)
