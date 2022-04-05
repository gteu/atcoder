N = int(input())


def f(a, b):
    return a ** 3 + a ** 2 * b + a * b ** 2 + b ** 3


ans = 10 ** 20
for i in range(10 ** 6 + 10):
    ng = -1
    ok = 10 ** 6 + 10
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if f(i, mid) >= N:
            ok = mid
        else:
            ng = mid
    ans = min(ans, f(i, ok))
print(ans)
