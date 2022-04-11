N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


if X == Y:
    dp = 0
    ans = 0
    for a in A:
        if X == a:
            dp += 1
        else:
            dp = 0
        ans += dp
    print(ans)
    exit()

dp = [0, 0, 0, 0]
ans = 0
for a in A:
    ndp = [0, 0, 0, 0]
    if Y < a < X:
        ndp[0] = dp[0] + 1
        ndp[1] = dp[1]
        ndp[2] = dp[2]
        ndp[3] = dp[3]
    elif Y == a:
        ndp[1] = dp[0] + dp[1] + 1
        ndp[3] = dp[2] + dp[3]
    elif X == a:
        ndp[2] = dp[0] + dp[2] + 1
        ndp[3] = dp[1] + dp[3]
    ans += ndp[3]
    dp = ndp
print(ans)
