N = int(input())
M = []
for _ in range(N):
    M.append(input())

flag = False
for i in range(N):
    for j in range(N):
        cnt = 0
        num = 0
        for k in range(6):
            if j + k < N:
                num += 1
                if M[i][j + k] == '#':
                    cnt += 1
        if num == 6 and cnt >= 4:
            flag = True

        cnt = 0
        num = 0
        for k in range(6):
            if j + k < N:
                num += 1
                if M[j + k][i] == '#':
                    cnt += 1
        if num == 6 and cnt >= 4:
            flag = True

for i in range(N):
    for j in range(N):
        for k in range(6):
            cnt = 0
            num = 0
        for k in range(6):
            if i + k < N and j + k < N:
                num += 1
                if M[i + k][j + k] == '#':
                    cnt += 1
        if num == 6 and cnt >= 4:
            flag = True

        cnt = 0
        num = 0
        for k in range(6):
            if 0 <= i - k and j + k < N:
                num += 1
                if M[i - k][j + k] == '#':
                    cnt += 1
        if num == 6 and cnt >= 4:
            flag = True
if flag:
    print('Yes')
else:
    print('No')
