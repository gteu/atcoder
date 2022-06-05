H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

ans = 0
dirs = [(0, 0), (1, 0), (0, 1), (1, 1)]
for i in range(H - 1):
    for j in range(W - 1):
        cnt = 0
        for di, dj in dirs:
            ni = i + di
            nj = j + dj
            if S[ni][nj] == '#':
                cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
