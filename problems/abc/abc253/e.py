MOD = 998244353
N, M, K = map(int, input().split())
dp = [0] + [1] * M
for i in range(N - 1):
    new_dp = [0] * (M + 1)
    for j in range(1, M + 1):
        if K == 0:
            new_dp[1] += dp[j]
        else:
            if j - K >= 1:
                new_dp[1] += dp[j]
                new_dp[j - K + 1] -= dp[j]
            if j + K <= M:
                new_dp[j + K] += dp[j]
    for j in range(M):
        new_dp[j + 1] += new_dp[j]
        new_dp[j + 1] %= MOD
    dp = new_dp
print(sum(dp) % MOD)
