H, W = map(int, input().split())
MOD = 10 ** 9 + 7
S = []
for _ in range(H):
    S.append(input())
dp = [[0] * W for _ in range(H)]
X = [[0] * W for _ in range(H)]
Y = [[0] * W for _ in range(H)]
Z = [[0] * W for _ in range(H)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            if i - 1 >= 0:
                X[i][j] = X[i - 1][j] + dp[i - 1][j]
                X[i][j] %= MOD
            if j - 1 >= 0:
                Y[i][j] = Y[i][j - 1] + dp[i][j - 1]
                Y[i][j] %= MOD
            if i - 1 >= 0 and j - 1 >= 0:
                Z[i][j] = Z[i - 1][j - 1] + dp[i - 1][j - 1]
                Z[i][j] %= MOD
        dp[i][j] += X[i][j] + Y[i][j] + Z[i][j]
        dp[i][j] %= MOD
print(dp[H - 1][W - 1])
