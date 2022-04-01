N = int(input())
A = list(map(int, input().split()))

s = []
cur = 0
for a in A:
    if not s:
        s.append([a, 1])
        cur += 1
    else:
        if s[-1][0] == a:
            if s[-1][1] == a - 1:
                s.pop()
                cur -= (a - 1)
            else:
                s[-1][1] += 1
                cur += 1
        else:
            s.append([a, 1])
            cur += 1
    print(cur)
