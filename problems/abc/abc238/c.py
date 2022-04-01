N = input()
MOD = 998244353

def fsum(k):
    s = 1
    e = 10 ** k - 10 ** (k - 1)
    return (s + e) * (e - s + 1) // 2 

def fsum2(k, e):
    s = 1
    e = e - 10 ** (k - 1) + 1
    return (s + e) * (e - s + 1) // 2 

ans = 0
for i in range(1, len(N) + 1):
    if i != len(N):
        ans = (ans + fsum(i)) % MOD
    else:
        ans = (ans + fsum2(i, int(N))) % MOD
print(ans)
