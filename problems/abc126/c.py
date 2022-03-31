N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    x = i
    cnt = 0
    while x < K:
        x *= 2
        cnt += 1
    ans += 1 / (2 ** cnt)
ans /= N
print(ans)
