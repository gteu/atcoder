N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
X = [0] * N
for a in A:
    a -= 1
    X[a] = 1
for i in L:
    cnt = 0
    for j, x in enumerate(X):
        if x == 1:
            cnt += 1
            if j != N - 1 and i == cnt and X[j + 1] == 0:
                X[j] = 0
                X[j + 1] = 1

ans = []
for i, x in enumerate(X):
    if x == 1:
        ans.append(i + 1)
print(*ans)
