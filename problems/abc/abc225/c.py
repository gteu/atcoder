N, M = map(int, input().split())
tmp = [0] * M
flg = True
template = '1234560'
for i in range(N):
    B = list(map(int, input().split()))
    B_mod = ''.join(list(map(lambda x: str(x % 7), B)))
    if B_mod not in template:
        flg = False
    for p, c in zip(B, B[1:]):
        if c - p != 1:
            flg = False
    if i == 0:
        tmp = B
    else:
        for j in range(M):
            if tmp[j] + 7 != B[j]:
                flg = False
    tmp = B
if flg:
    print('Yes')
else:
    print('No')
