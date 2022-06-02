import math


def sum_arith(f, l, n):
    return (f + l) * n // 2


N, A, B = map(int, input().split())
lcm = A * B // math.gcd(A, B)
ans = sum_arith(1, N, N) \
    - sum_arith(A, N // A * A, N // A) \
    - sum_arith(B, N // B * B, N // B) \
    + sum_arith(lcm, N // lcm * lcm, N // lcm)
print(ans)
