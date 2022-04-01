def solve(N, S):
    cnt = 0
    for i in range((N + 1) // 2):
        cnt *= 26
        cnt += (ord(S[i]) - ord('A'))
        cnt %= MOD
    return (cnt + (S[:(N + 1) // 2][::-1] <= S[N // 2:])) % MOD


T = int(input())
MOD = 998244353
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    ans.append(solve(N, S))
print(*ans, sep='\n')
