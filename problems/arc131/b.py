h, w = map(int, input().split())
c = []
for _ in range(h):
    c.append(input())

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(h):
    for j in range(w):
        colors = []
        for dir in dirs:
            if 