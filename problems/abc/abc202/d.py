def ncr(n, r):
    r = min(r, n - r)
    x, y = 1, 1
    for i in range(r):
        x = (x * (n - i))
        y = (y * (i + 1))

    return x // y


A, B, K = map(int, input().split())
cur = 0
ans = []
while A + B:
    d = ncr(A + B - 1, A - 1)
    if K <= cur + d and A > 0:
        ans.append('a')
        A -= 1
    else:
        ans.append('b')
        B -= 1
        cur += d
print(''.join(ans))
