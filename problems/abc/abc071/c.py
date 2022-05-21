from audioop import reverse
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
ctr = Counter(A)
L = []
for k, v in ctr.items():
    if v >= 2:
        L.append(k)
    v -= 2
    if v >= 2:
        L.append(k)
L.sort(reverse=True)
if len(L) >= 2:
    print(L[0] * L[1])
else:
    print(0)
