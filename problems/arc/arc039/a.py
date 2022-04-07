A, B = input().split()
ans = -1000
for i in range(3):
    for j in range(10):
        nA = int(A[:i] + str(j) + A[i + 1:])
        if nA >= 100:
            ans = max(ans, nA - int(B))
        nB = int(B[:i] + str(j) + B[i + 1:])
        if nB >= 100:
            ans = max(ans, int(A) - nB)
print(ans)
