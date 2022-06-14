X = input()
M = int(input())
N = len(X)

if N == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
    exit()


def is_ok(v):
    s = 0
    for i in range(N):
        s += int(X[N - i - 1]) * v ** i
        if s > M:
            return False
    return True


m = max([int(s) for s in X])
ok = m
ng = 10 ** 18 + 1
while ok + 1 < ng:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok - m)
