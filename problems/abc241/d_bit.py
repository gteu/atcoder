import typing


class FenwickTree:
    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n

    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s


Q = int(input())
bit = FenwickTree(2 * 10 ** 5 + 5)
X = set()
queries = []
for _ in range(Q):
    query = tuple(map(int, input().split()))
    queries.append(query)
    t, *q = query
    X.add(q[0])

x2i = {x: i for i, x in enumerate(sorted(X))}
i2x = {i: x for i, x in enumerate(sorted(X))}

ans = []
for query in queries:
    t, *q = query
    if t == 1:
        bit.add(x2i[q[0]], 1)
    elif t == 2:
        x, k = q
        ok = 0
        ng = x2i[x] + 1
        s = bit.sum(0, x2i[x] + 1)
        if s < k:
            ans.append(-1)
            continue
        while ok + 1 < ng:
            mid = (ok + ng) // 2
            if bit.sum(mid, x2i[x] + 1) >= k:
                ok = mid
            else:
                ng = mid
        ans.append(i2x[ok])
    else:
        x, k = q
        ng = x2i[x] - 1
        ok = bit._n
        s = bit.sum(x2i[x], bit._n)
        if s < k:
            ans.append(-1)
            continue
        while ng + 1 < ok:
            mid = (ok + ng) // 2
            if bit.sum(x2i[x], mid + 1) >= k:
                ok = mid
            else:
                ng = mid
        ans.append(i2x[ok])
print(*ans, sep='\n')
