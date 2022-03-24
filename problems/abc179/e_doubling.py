N, X, M = map(int, input().split())

dp_nxt = [[-1] * M for _ in range(41)]
dp_sum = [[-1] * M for _ in range(41)]
for i in range(M):
    dp_sum[0][i] = pow(i, 2, M)
    dp_nxt[0][i] = pow(i, 2, M)
for i in range(40):
    for j in range(M):
        dp_nxt[i + 1][j] = dp_nxt[i][dp_nxt[i][j]]
        dp_sum[i + 1][j] = dp_sum[i][j] + dp_sum[i][dp_nxt[i][j]]

N -= 1
ans = X
cur = X
for i in range(40):
    if N >> i & 1:
        ans += dp_sum[i][cur]
        cur = dp_nxt[i][cur]
print(ans)
