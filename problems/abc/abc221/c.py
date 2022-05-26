N = input()
ans = 0

for i in range(2 ** len(N)):
    L = []
    R = []
    for j in range(len(N)):
        if i >> j & 1:
            L.append(N[j])
        else:
            R.append(N[j])
    if not L or not R or all([l == '0' for l in L]) or all([r == '0' for r in R]):
        continue
    Ln = int(''.join(sorted(L, reverse=True)))
    Rn = int(''.join(sorted(R, reverse=True)))
    ans = max(ans, Ln * Rn)

print(ans)
