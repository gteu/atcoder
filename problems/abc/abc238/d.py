t = int(input())
for _ in range(t):
    a, s = map(int, input().split())
    xor = s - 2 * a
    if xor < 0 or xor & a:
        print("No")
    else:
        print("Yes")
