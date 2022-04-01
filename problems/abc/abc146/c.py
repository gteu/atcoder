A, B, X = map(int, input().split())
ok = 0
ng = 10 ** 9 + 1
while ng - ok > 1:
    mid = (ng + ok) // 2
    v = A * mid + B * len(str(mid))
    if v <= X:
        ok = mid
    else:
        ng = mid
print(ok)
