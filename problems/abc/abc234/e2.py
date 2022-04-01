x = int(input())

ans = float('inf')
for d in range(-9, 10):
    for i in range(1, 10):
        v = i
        while v < x:
            if 0 <= v % 10 + d < 10:
                v = v * 10 + v % 10 + d
            else:
                v = float('inf')
                break
        ans = min(ans, v)
print(ans)