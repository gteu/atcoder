N = int(input())
C = list(map(int, input().split()))
m = min(C)
mi = -1
for i in range(9):
    if C[i] == m:
        mi = i
cnt = N // m
r = N % m
ans = [mi + 1] * cnt
for i in range(cnt):
    for j in reversed(range(mi + 1, 9)):
        if r >= C[j] - m:
            ans[i] = j + 1
            r -= C[j] - m
            break
print(*ans, sep='')
