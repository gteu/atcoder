N = int(input())
S = list(map(int, input().split()))

L = [0] * (N + 2)
for i in range(1, N):
    if S[i] - S[i - 1] < 0:
        L[i - 1] = S[i - 1] - S[i]
    else:
        L[i + 2] = S[i] - S[i - 1]

for i in range(N):
    if S[i] < L[i] + L[i + 1] + L[i + 2]:
        print("No")
        exit()

print("Yes")
for i in range(L[0], S[0] + 1):
    ans = [0] * (N + 2)
    ans[0] = i
    for j in range(L[1], S[0] - ans[0] + 1):
        flg = False
        ans[1] = j
        for k in range(2, N + 2):
            ans[k] = S[k - 2] - ans[k - 1] - ans[k - 2]
            if ans[k] < L[k]:
                flg = True
                break
        if not flg:
            print(*ans)
            exit()
