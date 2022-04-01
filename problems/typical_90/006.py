N, K = map(int, input().split())
S = input()

nxt = [[-1] * 26 for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    for j in range(26):
        nxt[i][j] = nxt[i + 1][j]
    for j in range(26):
        if S[i] == chr(ord('a') + j):
            nxt[i][j] = i

ans = []
i = 0
while len(ans) < K:
    for j in range(26):
        if nxt[i][j] != -1 and nxt[i][j] <= N - K + len(ans):
            ans.append(chr(ord('a') + j))
            i = nxt[i][j] + 1
            break
print(''.join(ans))
