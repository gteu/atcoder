N = int(input())
if N % 2:
    exit()

ans = []
for i in range(2 ** N):
    S = ''
    for j in range(N):
        if i >> j & 1:
            S += '('
        else:
            S += ')'
    cnt = 0
    ok = True
    for s in S:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            ok = False
    if cnt == 0 and ok:
        ans.append(S)
ans.sort()
print(*ans, sep='\n')
