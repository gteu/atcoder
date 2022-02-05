from bisect import bisect_left

H, W, N = map(int, input().split())
X = set()
Y = set()
dots = []
for _ in range(N):
    x, y = map(int, input().split())
    X.add(x)
    Y.add(y)
    dots.append((x, y))
X = sorted(list(X))
Y = sorted(list(Y))

for x, y in dots:
    print(bisect_left(X, x) + 1, bisect_left(Y, y) + 1)