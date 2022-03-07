N = int(input())
C = input()

cnt = 0
l = 0
r = N - 1
while l < r:
    if C[l] == 'W' and C[r] == 'R':
        cnt += 1
        l += 1
        r -= 1
    elif C[l] == C[r] == 'W':
        r -= 1
    elif C[l] == C[r] == 'R':
        l += 1
    else:
        l += 1
        r -= 1
print(cnt)
