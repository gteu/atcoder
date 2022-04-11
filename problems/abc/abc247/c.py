N = int(input())

ans = []


def dfs(n):
    global ans
    if n == 1:
        ans.append(1)
        return
    dfs(n - 1)
    ans.append(n)
    dfs(n - 1)


dfs(N)
print(*ans)
