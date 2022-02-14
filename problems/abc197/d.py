from math import cos, sin, radians

N = int(input())
x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
xc, yc = (x0 + x1) / 2, (y0 + y1) / 2
r = radians(360 / N)

dx = (x0 - xc) * cos(r) - (y0 - yc) * sin(r)
dy = (x0 - xc) * sin(r) + (y0 - yc) * cos(r)

print(xc + dx, yc + dy)
