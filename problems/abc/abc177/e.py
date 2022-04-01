from math import gcd
N = int(input())
A = list(map(int, input().split()))


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


pd = PrimeDecomposer(10 ** 6 + 1)
prime_set = set()
pair_flag = True
set_flag = True
for a in A:
    primes = pd.decompose(a)
    for p in primes:
        if p in prime_set:
            pair_flag = False
    prime_set |= set(primes)

if pair_flag:
    print('pairwise coprime')
else:
    g = A[0]
    for a in A[1:]:
        g = gcd(g, a)
    if g == 1:
        print('setwise coprime')
    else:
        print('not coprime')
