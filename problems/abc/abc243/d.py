N, X = map(int, input().split())
S = input()
stack = []
for i in range(N):
    if S[i] == 'U' and stack and stack[-1] != 'U':
        stack.pop()
    else:
        stack.append(S[i])
for s in stack:
    if s == 'R':
        X = 2 * X + 1
    elif s == 'L':
        X *= 2
    else:
        X //= 2

print(X)
