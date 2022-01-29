import itertools
import math

n = int(input())
A = []
for _ in range(n):
    A.append(tuple(map(int, input().split())))

ans = set()
for a1, a2 in itertools.combinations(A, 2):
    x, y = a1[0] - a2[0], a1[1] - a2[1]
    d = math.gcd(x, y)
    ans.add((x // d, y // d))
    ans.add((-x // d, -y // d))

print(len(ans))