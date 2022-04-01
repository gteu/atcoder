N = int(input())
T = list(map(int, input().split()))

S = sum(T)
dp = [[False] * (S // 2 + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(S // 2 + 1):
        if j + T[i] < S // 2 + 1:
            dp[i + 1][j + T[i]] = dp[i + 1][j + T[i]] | dp[i][j]
        dp[i + 1][j] = dp[i + 1][j] | dp[i][j]

for i in range(S // 2, -1, -1):
    if dp[N][i]:
        print(S - i)
        exit()
