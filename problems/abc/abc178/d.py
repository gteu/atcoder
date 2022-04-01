MOD = 10 ** 9 + 7
S = int(input())
N = S // 3 + 1
dp = [[0] * (S + 1) for _ in range(N + 1)]
for i in range(3, S + 1):
    dp[0][i] = 1
for i in range(N):
    count = 0
    for j in range(3, S - 2):
        count += dp[i][j]
        dp[i + 1][j + 3] = count
        dp[i + 1][j + 3] %= MOD
ans = 0
for i in range(N + 1):
    ans = (ans + dp[i][S]) % MOD
print(ans)
