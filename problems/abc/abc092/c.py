N = int(input())
A = [0] + list(map(int, input().split())) + [0]

C = []
csum = 0
for p, c in zip(A, A[1:]):
    C.append(c - p)
    csum += abs(c - p)

for p, c in zip(C, C[1:]):
    if (p > 0 and c > 0) or (p < 0 and c < 0):
        print(csum)
    else:
        print(csum - min(abs(c), abs(p)) * 2)
