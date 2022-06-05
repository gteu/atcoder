N = int(input())
ans = [[] for _ in range(N)]
for i in range(N):
    for j in range(i + 1):
        if j == 0 or j == i:
            ans[i].append(1)
        else:
            ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])
for i in range(N):
    print(*ans[i])
