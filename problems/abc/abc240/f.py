T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = 0
    B = 0
    ans = 0
    for i in range(N):
        x, y = map(int, input().split())
        if i == 0:
            ans = x
        if x != 0:
            j = - B // x
            if B > 0 and j <= y:
                ans = max(ans, A + j * (2 * (B + x) + (j - 1) * x) // 2)
        A += y * (2 * (B + x) + (y - 1) * x) // 2
        B += x * y
        ans = max(ans, A)
    print(ans)
