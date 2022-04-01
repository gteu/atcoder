import pypyjit
import sys
sys.setrecursionlimit(300000)
pypyjit.set_param('max_unroll_recursion=-1')

N, M = map(int, input().split())
edges = [[] for _ in range(N)]
MOD = 998244353
for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    edges[U].append(V)
    edges[V].append(U)


def dfs(cur):
    visited[cur] = True
    global node_num, edge_num
    node_num += 1
    edge_num += len(edges[cur])
    for nxt in edges[cur]:
        if not visited[nxt]:
            dfs(nxt)


visited = [False] * N
ans = 1
for i in range(N):
    node_num = 0
    edge_num = 0
    if not visited[i]:
        dfs(i)
        if node_num == edge_num // 2:
            ans *= 2
            ans %= MOD
        else:
            ans = 0
print(ans)
