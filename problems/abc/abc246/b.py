import math
A, B = map(int, input().split())

s = math.sqrt(A * A + B * B)
print(A / s, B / s)
