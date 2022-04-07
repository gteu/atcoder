import math
N, X = map(int, input().split())
A = list(map(lambda x: abs(int(x) - X), input().split()))

g = A[0]
for a in A:
    g = math.gcd(g, a)
print(g)
