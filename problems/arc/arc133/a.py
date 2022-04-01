n = int(input())
A = list(map(int, input().split()))
cur = A[0]
for a in A:
    if a < cur:
        break
    else:
        cur = a

ans = []
for a in A:
    if a != cur:
        ans.append(a)
print(*ans, sep=" ")