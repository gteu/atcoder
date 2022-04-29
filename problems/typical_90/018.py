import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
ans = []
for _ in range(Q):
    E = int(input())
    theta = - 90 - 360 * E / T
    cy, cz = math.cos(math.radians(theta)) * L / 2, \
        math.sin(math.radians(theta)) * L / 2 + L / 2
    ans.append(math.degrees(math.atan(cz / math.sqrt(X ** 2 + (Y - cy) ** 2))))
print(*ans, sep='\n')
