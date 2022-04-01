N = int(input())
X, Y = map(int, input().split())
INF = 10 ** 9
MAX_NUM = 300
dp = [[[INF] * (MAX_NUM + 1) for _ in range(MAX_NUM + 1)]
      for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    a, b = map(int, input().split())
    for j in range(MAX_NUM + 1):
        for k in range(MAX_NUM + 1):
            dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k])
            dp[i + 1][min(j + a, X)][min(k + b, Y)] = \
                min(dp[i][j][k] + 1, dp[i + 1][min(j + a, X)][min(k + b, Y)])
            # if j + a <= MAX_NUM and k + b <= MAX_NUM
            # でダメな理由は、MAX_NUM を超えた場合に反映されないから（超えても OK な問題なのに）

if dp[N][X][Y] == INF:
    print(-1)
else:
    print(dp[N][X][Y])
