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
S = []
for _ in range(H):
    S.append(input())

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
edges = []
for i in range(H):
    for j in range(W):
        for k in range(4):
            di, dj = dirs[k]
            ni = i + di
            nj = j + dj
            if 0 <= ni < H and 0 <= nj < W and S[i][j] == '#' and S[ni][nj] == '.':
                edges.append((k, i, j))
uf = DSU(len(edges))
for i in range(len(edges)):
    for j in range(i + 1, len(edges)):
        k1, i1, j1 = edges[i]
        k2, i2, j2 = edges[j]
        if k1 == k2 and abs(i1 - i2) + abs(j1 - j2) <= 1:
            uf.merge(i, j)
print(len(uf.groups()))
