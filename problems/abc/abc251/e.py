N = int(input())
A = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(N + 1)]
for i, a in enumerate(A):
    if i == 0:
        continue
    elif i == 1:
        dp[i + 1][0] = a
        dp[i + 1][1] = a
    else:
        dp[i + 1][0] = min(dp[i][0] + a, dp[i][1] + a)
        dp[i + 1][1] = dp[i][0]

dp2 = [[0] * 2 for _ in range(N + 1)]
for i, a in enumerate(A):
    if i == 0:
        dp2[i + 1][0] = a
        dp2[i + 1][1] = a
    else:
        dp2[i + 1][0] = min(dp2[i][0] + a, dp2[i][1] + a)
        dp2[i + 1][1] = dp2[i][0]
print(min(dp[N][0], min(dp2[N])))
