from bisect import bisect_left

N = int(input())
A = []
T = []
for _ in range(N):
    x, y = map(int, input().split())
    T.append((x, 1))
    T.append((x + y, -1))
T.sort()

ans = [0] * (N + 1)
pre, person = 0, 0
for cur, count in T:
    ans[person] += (cur - pre)
    pre = cur
    person += count

print(*ans[1:])