N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

dp = [0] * (10)
dp[A[0]] = 1
for i in range(1, N):
    new_dp = [0] * (10)
    for j in range(10):
        new_dp[(j * A[i]) % 10] = (new_dp[(j * A[i]) % 10] + dp[j]) % MOD
        new_dp[(j + A[i]) % 10] = (new_dp[(j + A[i]) % 10] + dp[j]) % MOD
    dp = new_dp
print(*dp)