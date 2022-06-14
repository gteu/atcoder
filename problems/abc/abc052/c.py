class PrimeDecomposer:
    def __init__(self, n):
        self.d = [i for i in range(n)]
        m = int(n ** 0.5) + 1
        for q in range(2 * 2, n, 2):
            self.d[q] = 2
        for p in range(3, m, 2):
            if self.d[p] == p:
                for q in range(p * p, n, p + p):
                    if self.d[q] == q:
                        self.d[q] = p

    def decompose(self, x):
        decomposed = []
        while x != 1:
            decomposed.append(self.d[x])
            x //= self.d[x]
        return decomposed


N = int(input())
pd = PrimeDecomposer(N + 3)
MOD = 10 ** 9 + 7
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    for j in pd.decompose(i):
        cnt[j] += 1
ans = 1
for v in cnt:
    ans *= (v + 1)
    ans %= MOD
print(ans)
