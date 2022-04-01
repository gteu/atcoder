N, M = map(int, input().split())
A = list(map(int, input().split()))
to = [[] for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    to[X].append(Y)

dp = A.copy()
ans = - 10 ** 9
for i in range(N):
    for j in to[i]:
        dp[j] = min(dp[i], dp[j], A[j])
        ans = max(ans, A[j] - dp[i])

print(ans)
