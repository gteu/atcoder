t = int(input())
ans = []
for _ in range(t):
    a, s = map(int, input().split())
    a = str(format(a, "b"))
    zero = []
    for i in range(len(a)):
        if a[i] == '1':
            s -= 2 ** (len(a) - i - 1) * 2
        else:
            zero.append(len(a) - i - 1)
    
    zero = list(range(60, len(a) - 1, -1)) + zero
    for i in zero:
        if s >= 2 ** i:
            s -= 2 ** i
    if s == 0:
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep='\n')