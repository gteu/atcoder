N = int(input())
cnt = [[0] * 10 for _ in range(10)]
S = []
for i in range(N):
    S.append(input())

for i in range(10):
    for j in range(N):
        cnt[int(S[j][i])][i] += 1

ans = 100000
for i in range(10):
    tmp = -1
    j = 0
    while sum(cnt[i]):
        if cnt[i][j] > 0:
            cnt[i][j] -= 1
        j += 1
        j %= 10
        tmp += 1
    ans = min(ans, tmp)
print(ans)
