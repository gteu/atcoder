import typing


class DSU:
    '''
    Implement (union by size) + (path halving)

    Reference:
    Zvi Galil and Giuseppe F. Italiano,
    Data structures and algorithms for disjoint set union problems
    '''

    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        x = self.leader(a)
        y = self.leader(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n

        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n

        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n

        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> typing.List[typing.List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]

        result: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))


H, W = map(int, input().split())
Q = int(input())
uf = DSU(H * W + 10)
red = [[False] * W for _ in range(H)]
for _ in range(Q):
    t, *q = map(int, input().split())
    if t == 1:
        r, c = q
        r -= 1
        c -= 1
        red[r][c] = True
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + i, c + j
            if 0 <= nr < H and 0 <= nc < W and red[nr][nc]:
                uf.merge(r * W + c, nr * W + nc)
    else:
        ra, ca, rb, cb = q
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        if ra == rb and ca == cb:
            if red[ra][ca]:
                print('Yes')
            else:
                print('No')
        elif uf.same(ra * W + ca, rb * W + cb):
            print('Yes')
        else:
            print('No')
