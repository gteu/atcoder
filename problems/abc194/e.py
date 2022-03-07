N, M = map(int, input().split())
A = list(map(int, input().split()))

used = [0] * (N + 1)
for i in range(M):
    used[A[i]] += 1
for i in range(N + 1):
    if used[i] == 0:
        cur = i
        break

ans = cur
for i in range(N - M):
    used[A[i]] -= 1
    used[A[i + M]] += 1
    if used[A[i]] == 0:
        ans = min(ans, A[i])
print(ans)
