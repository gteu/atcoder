N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [True, True]

for i in range(N - 1):
    new_dp = [False, False]
    if dp[0]:
        if abs(A[i + 1] - A[i]) <= K:
            new_dp[0] = True
        if abs(B[i + 1] - A[i]) <= K:
            new_dp[1] = True
    if dp[1]:
        if abs(A[i + 1] - B[i]) <= K:
            new_dp[0] = True
        if abs(B[i + 1] - B[i]) <= K:
            new_dp[1] = True
    dp = new_dp

if dp[0] or dp[1]:
    print('Yes')
else:
    print('No')
