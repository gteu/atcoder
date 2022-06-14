X, A, D, N = map(int, input().split())
L = A + (N - 1) * D
if D == 0:
    print(abs(A - X))
    exit()
if D < 0:
    A, L = L, A
    D *= -1

if A <= X <= L:
    X -= A % D
    print(min(X % D, D - X % D))
elif X < A:
    print(A - X)
else:
    print(X - L)
