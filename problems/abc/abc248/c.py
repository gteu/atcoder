N, M, K = map(int, input().split())
MOD = 998244353
dp = [1] + [0] * K
for _ in range(N):
    ndp = [0] * (K + 1)
    for i in range(K + 1):
        for j in range(1, M + 1):
            if i + j <= K:
                ndp[i + j] += dp[i]
                ndp[i + j] %= MOD
    dp = ndp
print(sum(dp) % MOD)
