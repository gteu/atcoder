from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
acc = [0]
for a in A:
    acc.append(acc[-1] + a)
for _ in range(Q):
    X = int(input())
    ans = 0
    li = bisect_left(A, X)
    ans += X * li - acc[li]
    ri = bisect_right(A, X)
    ans += (acc[N] - acc[ri]) - X * (N - ri)
    print(ans)
