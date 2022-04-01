N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-1] * N for _ in range(41)]
for i, a in enumerate(A):
    dp[0][i] = a
for i in range(40):
    for j in range(N):
        dp[i + 1][j] = dp[i][j] + dp[i][(j + dp[i][j]) % N]

ans = 0
for i in range(40):
    if K >> i & 1:
        ans += dp[i][ans % N]
print(ans)
