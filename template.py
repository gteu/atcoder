# Yes
def yes(bool):
    if bool:
        print("Yes")
    else:
        print("No")

# 1行 1文字 読み取る
N = int(input())

# 1行 複数個 読み取る(それぞれ)
x, y, z = map(int, input().split())

# 1行 複数個 読み取る(リスト, str)
str_list = input().split()

# 1行 複数個 読み取る(リスト, int)
int_list = list(map(int, input().split()))

# 再帰の深さ制限
import sys
sys.setrecursionlimit(300000)

# PyPy で再帰速くなるやつ
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

# bit 全探索の型
for i in range(2 ** N):
    for j in range(N):
        if i >> j & 1:
            # 処理内容

# modの組み合わせ。ncrを何回も計算する場合は一回初期化するこれの方が速い。
mod = 998244353

class Combination:
    def __init__(self, n):
        self.facts = [1 for _ in range(n + 1)]
        self.invs = [1 for _ in range(n + 1)]

        for i in range(1, n + 1):
            self.facts[i] = self.facts[i - 1] * i % mod
        self.invs[n] = pow(self.facts[n], mod - 2, mod)
        for i in range(1, n + 1):
            self.invs[n - i] = self.invs[n - i + 1] * (n - i + 1) % mod

    def ncr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        else:
            return self.facts[n] * self.invs[r] * self.invs[n - r] % mod

    def npr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        return self.facts[n] * self.invs[n - r] % mod

    def nhr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        else:
            return self.ncr(n + r - 1, n - 1)

# modのncr。上のだと初期化のNが大きい時にきつい。1回だけ求める場合はこの方が速い。
mod = 998244353

def ncr(n, r, mod):
    r = min(r, n - r)
    x, y = 1, 1
    for i in range(r):
        x = (x * (n - i)) % mod
        y = (y * (i + 1)) % mod
    
    return x * pow(y, mod - 2, mod) % mod


# 素因数分解(試し割り法) → 事前に素数テーブル作った方が速い
def prime_decompose(x):
    decomposed = []
    for i in range(2, int(pow(x, 0.5)) + 1):
        while x % i == 0:
            x //= i
            decomposed.append(i)
    if x > 1:
        decomposed.append(x)
    return decomposed

# 約数列挙
def get_divisor(x):
    divisor = []
    for i in range(1, int(pow(x, 0.5)) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x//i:
                divisor.append(x // i)

    return divisor

# 素数列挙(エラトステネスの篩)
def make_prime(n):
    # n未満の素数を返す
    is_prime = [False] * (n)
    is_prime[2] = True
    for i in range(3, n, 2):
        is_prime[i] = True
    m = int(n ** 0.5) + 1
    for p in range(3, m, 2):
        if is_prime[p]:
            for q in range(p * p, n, p + p):
                is_prime[q] = False

    ret = []
    for i in range(n):
        if is_prime[i]:
            ret.append(i)

    return ret

# LIS(Longest Increasing Subsequence) (狭義単調増加の場合)
def lis(S):
    from bisect import bisect_left
    L = [S[0]]
    for s in S[1:]:
        if s > L[-1]:
            L.append(s)
        else:
            L[bisect_left(L, s)] = s
    return len(L)

# LIS(Longest Increasing Subsequence) (広義単調増加の場合)
def lis2(S):
    from bisect import bisect_right
    L = [S[0]]
    for s in S[1:]:
        if s >= L[-1]:
            L.append(s)
        else:
            L[bisect_right(L, s)] = s
    return len(L) 

# ダイクストラ
def dij(G, s):
    """Dijkstra's algorithm
    Args:
        G (List[List[int, int]]): [adjacent node, weight] 
        s (int): starting index

    Returns:
        d (List[int]): distances
    """
    from heapq import heappush, heappop

    INF = 10 ** 18
    d = [INF] * len(G)
    d[s] = 0
    q = [(0, s)]
    while q:
        cur_d, cur_i = heappop(q)
        if cur_d > d[cur_i]:
            continue
        for nxt_i, w in G[cur_i]:
            nxt_d = cur_d + w
            if d[nxt_i] > nxt_d:
                d[nxt_i] = nxt_d
                heappush(q, (nxt_d, nxt_i))
    return d