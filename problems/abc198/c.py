R, X, Y = map(int, input().split())
G = X * X + Y * Y
cur = 0
if R ** 2 == G:
    print(1)
    exit()
while -1:
    if (R * cur + 2 * R) ** 2 >= G:
        print(cur + 2)
        exit()
    cur += 1
