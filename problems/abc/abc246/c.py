N, K, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] // X <= K:
        K -= A[i] // X
        A[i] %= X
    elif A[i] > K * X:
        A[i] -= K * X
        K = 0

A.sort(reverse=True)
i = 0
while K > 0 and i < N:
    K -= 1
    A[i] = 0
    i += 1
print(sum(A))
