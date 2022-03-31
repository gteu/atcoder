N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]


def is_ok(v):
    cur = 0
    cnt = 0
    for p, c in zip(A, A[1:]):
        if cur + c - p < v:
            cur += c - p
        else:
            cur = 0
            cnt += 1
    return cnt > K


ok = 0
ng = L
while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
