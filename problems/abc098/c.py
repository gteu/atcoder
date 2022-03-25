N = int(input())
S = input()
west = [True] * N

for i in range(1, N):
    if S[i] == 'E':
        west[i] = False

cnt = N - 1 - sum(west[1:])
ans = cnt

for i in range(N - 1):
    if S[i] == 'W':
        cnt += 1
    if S[i + 1] == 'E':
        cnt -= 1
    ans = min(ans, cnt)
print(ans)
