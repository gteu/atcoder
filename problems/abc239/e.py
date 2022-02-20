import sys
sys.setrecursionlimit(300000)

N, Q = map(int, input().split())
X = list(map(int, input().split()))
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

order = [[] for _ in range(N)]


def dfs(cur):
    visited[cur] = True
    order[cur] += [X[cur]]
    if not edge[cur]:
        order[cur] = [X[cur]]
    for nxt in edge[cur]:
        if not visited[nxt]:
            dfs(nxt)
            order[cur] += order[nxt]
    order[cur].sort(reverse=True)
    order[cur] = order[cur][:20]


visited = [False] * N
dfs(0)

for i in range(Q):
    V, K = map(int, input().split())
    print(order[V - 1][K - 1])
