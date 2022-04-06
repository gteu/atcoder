import sys
input = sys.stdin.buffer.readline
N, K = map(int, input().split())
MOD = 998244353
segs = []
for _ in range(K):
    L, R = map(int, input().split())
    R += 1
    segs.append((L, R))

dp = [0] * N
dp[0] = 1
dp[1] = -1
for i in range(N):
    if i != 0:
        dp[i] += dp[i - 1]
    for L, R in segs:
        if i + L < N:
            dp[i + L] += dp[i]
            dp[i + L] %= MOD
        if i + R < N:
            dp[i + R] -= dp[i]
            dp[i + R] %= MOD
print(dp[N - 1] % MOD)
