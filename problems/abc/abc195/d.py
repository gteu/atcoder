from bisect import bisect_left

N, M, Q = map(int, input().split())
W = []
for _ in range(N):
    W.append(tuple(map(int, input().split())))
W.sort(reverse=True, key=lambda x: x[1])
X = list(map(int, input().split()))

for _ in range(Q):
    l, r = map(int, input().split())
    cur_X = X[:l - 1] + X[r:]
    cur_X.sort()
    ans = 0
    for w, v in W:
        i = bisect_left(cur_X, w)
        if i < len(cur_X):
            ans += v
            cur_X.pop(i)
    print(ans)
