N = int(input())
c0, c1 = 1, 1
for i in range(N):
    S = input()
    if S == 'AND':
        c0, c1 = c0 * 2 + c1, c1
    else:
        c0, c1 = c0, c0 + 2 * c1
print(c1)
