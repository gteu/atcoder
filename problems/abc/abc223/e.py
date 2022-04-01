H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MOD = 998244353

dp = [[0] * 2 for _ in range(2)]
dp[x1 == x2][y1 == y2] = 1

for i in range(K):
    nxt_dp = [[0] * 2 for _ in range(2)]
    nxt_dp[1][0] += (W - 1) * dp[1][1]
    nxt_dp[0][1] += (H - 1) * dp[1][1]

    nxt_dp[1][1] += dp[1][0]
    nxt_dp[1][0] += (W - 2) * dp[1][0]
    nxt_dp[0][0] += (H - 1) * dp[1][0]

    nxt_dp[1][1] += dp[0][1]
    nxt_dp[0][1] += (H - 2) * dp[0][1]
    nxt_dp[0][0] += (W - 1) * dp[0][1]

    nxt_dp[0][1] += dp[0][0]
    nxt_dp[1][0] += dp[0][0]
    nxt_dp[0][0] += (H + W - 4) * dp[0][0]

    for j in range(2):
        for k in range(2):
            nxt_dp[j][k] %= MOD

    dp = nxt_dp

print(dp[1][1])
