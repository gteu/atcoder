X1, Y1, X2, Y2 = map(int, input().split())

dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
pos = []
for x1, y1 in dirs:
    for x2, y2 in dirs:
        pos.append((x1+x2, y1+y2))

if ((X2 - X1), (Y2 - Y1)) in pos:
    print('Yes')
else:
    print('No')
