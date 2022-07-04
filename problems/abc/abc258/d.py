N, X = map(int, input().split())
ans = 10 ** 30
cur = 0
for _ in range(N):
    A, B = map(int, input().split())
    cur += A + B
    X -= 1
    if X >= 0:
        ans = min(ans, cur + X * B)
print(ans)
