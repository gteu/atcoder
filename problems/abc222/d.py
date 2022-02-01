N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

dp = [[0] * (3001) for _ in range(N)]

for j in range(A[0], B[0] + 1):
    dp[0][j] = 1

for i in range(1, N):
    csum = 0
    for j in range(3001):
        csum = (csum + dp[i - 1][j]) % MOD
        if A[i] <= j <= B[i]:
            dp[i][j] = csum 

print(sum(dp[N - 1]) % MOD)