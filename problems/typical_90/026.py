import sys
sys.setrecursionlimit(300000)

N = int(input())
to = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    to[A].append(B)
    to[B].append(A)

odd = []
even = []
d_cur = 0


def dfs(cur, pre):
    global d_cur
    if d_cur % 2:
        odd.append(cur + 1)
    else:
        even.append(cur + 1)
    d_cur += 1
    for nxt in to[cur]:
        if nxt != pre:
            dfs(nxt, cur)
    d_cur -= 1


dfs(0, -1)
if len(odd) >= N // 2:
    print(*odd[:N // 2])
else:
    print(*even[:N // 2])
