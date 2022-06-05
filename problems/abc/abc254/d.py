from bisect import bisect_left
from collections import Counter


def prime_decompose(x):
    decomposed = []
    for i in range(2, int(pow(x, 0.5)) + 1):
        while x % i == 0:
            x //= i
            decomposed.append(i)
    if x > 1:
        decomposed.append(x)
    return decomposed


N = int(input())
A = []
for i in range(N + 1):
    if i ** 2 <= N:
        A.append(i ** 2)
    else:
        break

ans = 0
for i in range(1, N + 1):
    cnt = Counter(prime_decompose(i))
    base = 1
    for k, v in cnt.items():
        if v % 2 == 1:
            base *= k
    ok = 0
    ng = len(A)
    while ok + 1 < ng:
        mid = (ok + ng) // 2
        if A[mid] * base <= N:
            ok = mid
        else:
            ng = mid
    ans += ok
print(ans)
