N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

diff = []
for p, c in zip(X, X[1:]):
    diff.append(c - p)
diff.sort()
if M - N < 0:
    print(0)
else:
    print(sum(diff[:M - N]))
