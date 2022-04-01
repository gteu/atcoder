import sys
sys.setrecursionlimit(300000)

N = int(input())
to = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    to[a].append(b)
    to[b].append(a)

for i in range(N + 1):
    to[i].sort()

ans = []
def dfs(cur, pre):
    ans.append(cur)
    for nxt in to[cur]:
        if nxt != pre:
            dfs(nxt, cur)
            ans.append(cur)

dfs(1, -1)
print(*ans)