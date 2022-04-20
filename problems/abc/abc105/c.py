N = int(input())
if N == 0:
    print(0)
    exit()

ans = []
d = 0
while N != 0:
    if N % 2 == 1:
        ans.append(1)
        N -= (-1) ** (d % 2)
    else:
        ans.append(0)
    N //= 2
    d += 1
ans.reverse()
print(*ans, sep='')
