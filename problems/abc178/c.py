N = int(input())
MOD = 10 ** 9 + 7
if N == 1:
    print(0)
else:
    ans = (pow(10, N, MOD) - 2 * pow(9, N, MOD) + pow(8, N, MOD)) % MOD
    print(ans)
