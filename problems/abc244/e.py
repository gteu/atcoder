N, M, K, S, T, X = map(int, input().split())
to = [[] for _ in range(N)]
MOD = 998244353
for _ in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    to[U].append(V)
    to[V].append(U)

S -= 1
T -= 1
X -= 1
dp = [[[0] * 2 for _ in range(N)] for _ in range(K + 1)]
dp[0][S][0] = 1

for i in range(K):
    for j in range(N):
        for nxt in to[j]:
            if nxt == X:
                dp[i + 1][nxt][1] += dp[i][j][0]
                dp[i + 1][nxt][0] += dp[i][j][1]
            else:
                dp[i + 1][nxt][0] += dp[i][j][0]
                dp[i + 1][nxt][1] += dp[i][j][1]
            dp[i + 1][nxt][0] %= MOD
            dp[i + 1][nxt][1] %= MOD
print(dp[K][T][0])
