N, K = map(int, input().split())
A = list(map(int, input().split()))


def is_ok(x):
    cnt = 0
    for a in A:
        cnt += (a - 1) // x
    return cnt <= K


ok = 10 ** 10
ng = 0
while ng + 1 < ok:
    mid = (ng + ok) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
