N, M = map(int, input().split())
H = list(map(int, input().split()))
to = [set() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    to[u].add(v)
    to[v].add(u)

visited = [False] * N

ans = -10 ** 9
def dfs(cur, s):
    global ans
    if visited[cur]:
        return s
    visited[cur] = True
    for nxt in to[cur]:
        if not visited[nxt]:
            if H[cur] > H[nxt]:
                ans = max(s, dfs(nxt, s + H[cur] - H[nxt]))
            else:
                ans = max(s, dfs(nxt, s + 2 * H[cur] - 2 * H[nxt]))
        print(cur, nxt, ans)
    visited[cur] = False
    return max(ans, s)

dfs(0, 0)
print(ans)