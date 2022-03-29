H, W, A, B = map(int, input().split())
used = [[False] * W for _ in range(H)]
ans = 0


def dfs(i, j, a, b):
    if i >= H:
        i %= H
        j += 1
    if j == W:
        global ans
        ans += 1
        return
    if used[i][j]:
        dfs(i + 1, j, a, b)
        return
    used[i][j] = True
    if b:
        dfs(i + 1, j, a, b - 1)
    if a:
        if j + 1 < W and not used[i][j + 1]:
            used[i][j + 1] = True
            dfs(i + 1, j, a - 1, b)
            used[i][j + 1] = False
        if i + 1 < H and not used[i + 1][j]:
            used[i + 1][j] = True
            dfs(i + 1, j, a - 1, b)
            used[i + 1][j] = False
    used[i][j] = False


dfs(0, 0, A, B)
print(ans)
