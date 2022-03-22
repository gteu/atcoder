import math

L, R = map(int, input().split())

for i in range(R - L, 0, -1):
    l = L
    r = L + i
    while r <= R:
        if math.gcd(l, r) == 1:
            print(i)
            exit()
        l += 1
        r += 1
