N, X = map(int, input().split())
L = [(1, 1)]
for i in range(N):
    ln, pn = L[-1]
    L.append((3 + 2 * ln, 1 + 2 * pn))

ci = 1
cl = N - 1
ans = 0
while -1:
    if ci == X:
        if cl == -1:
            ans += 1
        print(ans)
        exit()
    ci += 1
    if X < ci + L[cl][0]:
        cl -= 1
        continue
    ci += L[cl][0]
    ans += L[cl][1] + 1
    if ci == X:
        print(ans)
        exit()
    ci += 1
    if X < ci + L[cl][0]:
        cl -= 1
        continue
    ci += L[cl][0]
    ans += L[cl][1]
    if ci == X:
        print(ans)
        exit()
