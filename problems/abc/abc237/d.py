N = int(input())
S = input()

ans = [0] * (N + 1)

cur_r = N
cur_l = 0
for i in range(N):
    if S[i] == "L":
        ans[cur_r] = i 
        cur_r -= 1
    else:
        ans[cur_l] = i
        cur_l += 1
ans[cur_l] = N
print(*ans)