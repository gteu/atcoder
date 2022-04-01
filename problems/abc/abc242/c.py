MOD = 998244353
N = int(input())
dp = [[0] * 9 for _ in range(N)]
for i in range(9):
    dp[0][i] = 1
for i in range(N - 1):
    for j in range(9):
        for k in range(max(0, j - 1), min(j + 2, 9)):
            dp[i + 1][k] += dp[i][j]
            dp[i + 1][k] %= MOD
print(sum(dp[N - 1]) % MOD)
