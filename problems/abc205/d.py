from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
new_A = []
for i, a in enumerate(A):
    new_A.append(a - i - 1)
ans = []
for _ in range(Q):
    K = int(input())
    i = bisect_left(new_A, K)
    if i == 0:
        ans.append(K)
    else:
        ans.append(A[i - 1] + K - new_A[i - 1])
print(*ans, sep='\n')
