from collections import deque

a, n = map(int, input().split())
q = deque([1])
dp = [-1] * (10 ** len(str(n)))
dp[1] = 0

while q:
    v = q.popleft()

    next = v * a
    if next < len(dp) and dp[next] == -1:
        dp[next] = dp[v] + 1
        q.append(next)

    if v > 10 and v % 10 != 0:
        next = int(str(v)[-1] + str(v)[:-1])
        if next < len(dp) and dp[next] == -1:
            dp[next] = dp[v] + 1
            q.append(next)

print(dp[n])