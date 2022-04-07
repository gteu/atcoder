N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 10 ** 10
for i in range(N - K + 1):
    l = X[i]
    r = X[i + K - 1]
    if (l < 0 and r < 0) or (l > 0 and r > 0):
        ans = min(ans, max(abs(l), abs(r)))
    else:
        ans = min(ans, r - l + min(abs(l), abs(r)))
print(ans)
