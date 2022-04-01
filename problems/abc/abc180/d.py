X, Y, A, B = map(int, input().split())
ans = 0
while X * A < Y and X * A < B / (A - 1):
    X *= A
    ans += 1
ans += (Y - X - 1) // B
print(ans)
