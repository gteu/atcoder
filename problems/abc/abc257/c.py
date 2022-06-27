from bisect import bisect_left, bisect_right

N = int(input())
S = input()
W = list(map(int, input().split()))
A = []
C = []
for i, s in enumerate(S):
    if s == '1':
        A.append(W[i])
    else:
        C.append(W[i])
A.sort()
C.sort()
ans = 0
for a in W:
    for d in range(-1, 2):
        x = a + d
        tmp = 0
        i = bisect_left(A, x)
        tmp += len(A) - i
        j = bisect_left(C, x)
        tmp += j
        ans = max(tmp, ans)
print(ans)
