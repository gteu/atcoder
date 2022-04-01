S = input()
must = []
opt = []
for i, s in enumerate(S):
    if s == 'o':
        must.append(str(i))
    elif s == '?':
        opt.append(str(i))

ans = 0
for i in range(0, 10000):
    P = list(str(i).zfill(4))
    is_ans = True
    for v in must:
        if v not in P:
            is_ans = False
            break
    for p in P:
        if p not in must and p not in opt:
            is_ans = False
            break
    ans += is_ans

print(ans)
