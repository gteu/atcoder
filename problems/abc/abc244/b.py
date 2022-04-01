N = int(input())
T = input()
x, y = 0, 0
dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
cur = 0
for t in T:
    if t == 'S':
        x += dir[cur][0]
        y += dir[cur][1]
    else:
        cur += 1
        cur %= 4
print(x, y)
