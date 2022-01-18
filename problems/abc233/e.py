xs = input()
x_sum = sum(map(int, xs))

ans = ""
up = 0
for x in reversed(xs):
    up += x_sum
    ans += str(up)[-1]
    if len(str(up)) > 1:
        up = int(str(up)[:-1])
    else:
        up = 0
    x_sum -= int(x)
if up != 0:
    ans += str(up)

print(ans[::-1])