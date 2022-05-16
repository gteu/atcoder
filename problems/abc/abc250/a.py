H, W = map(int, input().split())
R, C = map(int, input().split())
ans = 0
for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    if 0 < R + i <= H and 0 < C + j <= W:
        ans += 1
print(ans)
