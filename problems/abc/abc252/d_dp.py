from collections import Counter
N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

dp = [0] * 5
dp[0] = 1
for k, v in cnt.items():
    new_dp = [0] * 5
    for i in range(4):
        new_dp[i + 1] += dp[i] * v
        new_dp[i] += dp[i]
    dp = new_dp
print(new_dp[3])
