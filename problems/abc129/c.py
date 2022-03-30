N, M = map(int, input().split())
A = set()
for i in range(M):
    A.add(int(input()))
MOD = 1000000007

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
    if i + 1 not in A:
        dp[i + 1] += dp[i]
        dp[i + 1] %= MOD
    if i + 2 < N + 1 and i + 2 not in A:
        dp[i + 2] += dp[i]
        dp[i + 2] %= MOD
print(dp[N])
