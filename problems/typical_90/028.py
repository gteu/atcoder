N = int(input())
dp = [[0] * 1001 for _ in range(1001)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    dp[lx][ly] += 1
    dp[rx][ly] -= 1
    dp[lx][ry] -= 1
    dp[rx][ry] += 1

for i in range(1000):
    for j in range(1001):
        dp[i + 1][j] += dp[i][j]

for i in range(1001):
    for j in range(1000):
        dp[i][j + 1] += dp[i][j]

cnt = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        cnt[dp[i][j]] += 1

print(*cnt[1:], sep='\n')
