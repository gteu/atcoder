import pypyjit
import sys
sys.setrecursionlimit(300000)
pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
C = list(map(int, input().split()))
edge = [[] for _ in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edge[A].append(B)
    edge[B].append(A)

cnt = [0] * (10 ** 5 + 1)
ans = []


def dfs(cur, pre):
    if cnt[C[cur]] == 0:
        ans.append(cur + 1)
    cnt[C[cur]] += 1
    for nxt in edge[cur]:
        if nxt != pre:
            dfs(nxt, cur)
    cnt[C[cur]] -= 1


dfs(0, -1)
ans.sort()
print(*ans, sep='\n')
