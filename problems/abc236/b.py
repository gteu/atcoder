from collections import Counter

n = int(input())
A = list(map(int, input().split()))
c = Counter(A)
for k, v in c.items():
    if v != 4:
        print(k)