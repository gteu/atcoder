S = input()
ref = 'chokudai'
MOD = 10 ** 9 + 7
dp = [1] + [0] * len(ref)
for s in S:
    if s in ref:
        i = ref.index(s)
        dp[i + 1] = (dp[i] + dp[i + 1]) % MOD
print(dp[-1])
