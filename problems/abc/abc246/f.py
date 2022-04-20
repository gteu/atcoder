MOD = 998244353
N, L = map(int, input().split())
S = []
for _ in range(N):
    n = 0
    for s in input():
        n += 2 ** (ord(s) - ord('a'))
    S.append(n)

ans = 0
for i in range(1, 2 ** N):
    cur = 2 ** 26 - 1
    c = 0
    for j in range(N):
        if i >> j & 1:
            cur &= S[j]
            c += 1

    cnt = bin(cur).count('1')
    if c % 2 == 0:
        ans -= pow(cnt, L, MOD)
    else:
        ans += pow(cnt, L, MOD)
    ans %= MOD
print(ans)
