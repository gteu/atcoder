import sys
input = sys.stdin.readline

H, W = map(int, input().split())
A = []
INF = 10 ** 9
for i in range(H):
    A.append(list(input()))

for i in range(H):
    for j in range(W):
        A[i][j] = 1 if A[i][j] == '+' else -1

dp = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        dp[i][j] = INF if (i + j) % 2 else -INF

dp[-1][-1] = 0
for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        if (i + j) % 2 == 0:
            if i + 1 < H:
                dp[i][j] = max(dp[i][j], dp[i + 1][j] + A[i + 1][j])
            if j + 1 < W:
                dp[i][j] = max(dp[i][j], dp[i][j + 1] + A[i][j + 1])
        else:
            if i + 1 < H:
                dp[i][j] = min(dp[i][j], dp[i + 1][j] - A[i + 1][j])
            if j + 1 < W:
                dp[i][j] = min(dp[i][j], dp[i][j + 1] - A[i][j + 1])

if dp[0][0] < 0:
    print('Aoki')
elif dp[0][0] > 0:
    print('Takahashi')
else:
    print('Draw')
