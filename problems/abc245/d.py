N, M = map(int, input().split())
A = list(map(int, input().split()))
A.reverse()
C = list(map(int, input().split()))
C.reverse()
B = [0] * (M + 1)

for i in range(M + 1):
    for j in range(-100, 101):
        B[i] = j
        tmp = 0
        for k in range(i + 1):
            if i - k <= N:
                tmp += A[i - k] * B[k]
        if tmp == C[i]:
            break
B.reverse()
print(*B)
