N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 18


def dfs(i, cur_xor, cur_or):
    global ans
    if i == N:
        ans = min(cur_xor ^ cur_or, ans)
    else:
        dfs(i + 1, cur_xor, cur_or | A[i])
        dfs(i + 1, cur_xor ^ cur_or, A[i])


dfs(0, 0, 0)
print(ans)
