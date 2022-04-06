A, B, C = map(int, input().split())

dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
dp[A][B][C] = 1

for x in range(100):
    for y in range(100):
        for z in range(100):
            if x + y + z == 0:
                continue
            dp[x + 1][y][z] += dp[x][y][z] * x / (x + y + z)
            dp[x][y + 1][z] += dp[x][y][z] * y / (x + y + z)
            dp[x][y][z + 1] += dp[x][y][z] * z / (x + y + z)

ans = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i == 100 or j == 100 or k == 100:
                ans += dp[i][j][k] * (i + j + k - A - B - C)
print(ans)
