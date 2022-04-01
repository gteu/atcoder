from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()

Q = int(input())
ans = []
for _ in range(Q):
    B = int(input())
    i = bisect_left(A, B)
    if i == N:
        ans.append(abs(A[N - 1] - B))
    elif i > 0:
        ans.append(min(abs(A[i] - B), abs(A[i - 1] - B)))
    else:
        ans.append(abs(A[0] - B))
print(*ans, sep='\n')
