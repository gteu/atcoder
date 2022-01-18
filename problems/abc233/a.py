x, y = map(int, input().split())
ans = (y-x) // 10
if (y-x) % 10:
    ans += 1
print(max(0, ans))