A = list(map(int, input().split()))
pre = 0
for i in range(3):
    pre = A[pre]
print(pre)
