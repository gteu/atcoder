from math import gcd
A, B, C, D = map(int, input().split())

lcm = C * D // gcd(C, D)
q1 = B // C - (A - 1) // C
q2 = B // D - (A - 1) // D
q3 = B // lcm - (A - 1) // lcm
print(B - A + 1 - q1 - q2 + q3)
