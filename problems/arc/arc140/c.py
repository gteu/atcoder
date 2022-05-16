import sys
sys.setrecursionlimit(300000)
N, X = map(int, input().split())
X -= 1
used = [False] * N
used[X] = True
ans_v = 0
ans = None
tmp = []


def dfs(cur, d, joy, n):
    global ans_v, ans
    if n == N:
        if joy > ans_v:
            ans = tmp[:]
            ans_v = joy
    if 0 <= cur + d + 1 < N and not used[cur + d + 1]:
        used[cur + d + 1] = True
        tmp.append(cur + d + 1)
        dfs(cur + d + 1, d + 1, joy + 1, n + 1)
        tmp.pop()
        used[cur + d + 1] = False
    if 0 <= cur - d - 1 < N and not used[cur - d - 1]:
        used[cur - d - 1] = True
        tmp.append(cur + d - 1)
        dfs(cur - d - 1, d + 1, joy + 1, n + 1)
        tmp.pop()
        used[cur - d - 1] = False
    if 0 <= cur + d < N and not used[cur + d]:
        used[cur + d] = True
        tmp.append(cur + d)
        dfs(cur + d, d, joy, n + 1)
        tmp.pop()
        used[cur + d] = False
    if 0 <= cur - d < N and not used[cur - d]:
        used[cur - d - 1] = True
        tmp.append(cur - d)
        dfs(cur - d, d, joy, n + 1)
        tmp.pop()
        used[cur - d] = False


tmp.append(X)
dfs(X, 1, 1, 1)
print(*ans)
