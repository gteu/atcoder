N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

d = 0
for a, b in zip(A, B):
    d += abs(a - b)
if K >= d and K % 2 == d % 2:
    print('Yes')
else:
    print('No')
