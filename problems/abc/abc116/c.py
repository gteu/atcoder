N = int(input())
H = list(map(int, input().split()))

ans = 0
while sum(H):
    flag = False
    for i in range(N):
        if H[i] != 0:
            if not flag:
                ans += 1
            H[i] -= 1
            flag = True
        else:
            flag = False
    flag = False
print(ans)
