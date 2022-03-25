N, K = map(int, input().split())
S = input()
if N == 1:
    print(1)
    exit()
zero = 1 if S[0] == '0' else 0
j = 0
ans = 0
for i in range(N - 1):
    while zero <= K:
        if j == N - 1:
            if S[j] == '0':
                zero += 1
            break
        elif S[j] == '1' and S[j + 1] == '0':
            if zero == K:
                break
            zero += 1
        j += 1
    ans = max(ans, j - i + 1)
    if S[i] == '0' and S[i + 1] == '1':
        zero -= 1
print(ans)
