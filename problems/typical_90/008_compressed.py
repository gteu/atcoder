N = int(input())
S = input()
MOD = 10 ** 9 + 7

ref = 'atcoder'
dp = [0] * 8
dp[0] = 1

for i in range(N):
    for j in reversed(range(7)):
        if S[i] == ref[j]:
            dp[j + 1] += dp[j]
            dp[j + 1] %= MOD
print(dp[-1])
