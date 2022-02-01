N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

def turn(M):
    M_ = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            M_[N - 1 - j][i] = M[i][j]
    return M_

def sharp(M):
    x, y = set(), set()
    for i in range(N):
        for j in range(N):
            if M[i][j] == '#':
                x.add(i)
                y.add(j)
    return sorted(list(x)), sorted(list(y))

def same(U, V):
    for i in range(len(U)):
        for j in range(len(U[0])):
            if U[i][j] != V[i][j]:
                return False
    return True

def shift(M, x, y):
    M_ = [['.'] * N for _ in range(N)]
    for i in range(N - x):
        for j in range(N - y):
            M_[i][j] = M[i + x][j + y]
    return M_
            

TX, TY = sharp(T)
shift_T = (TX[0], TY[0])

for _ in range(4):
    S = turn(S)
    SX, SY = sharp(S)
    shift_S = (SX[0], SY[0])
    if same(shift(S, *shift_S), shift(T, *shift_T)):
        print("Yes")
        exit()

print("No")
    