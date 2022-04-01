N, W = map(int, input().split())
changes = []
for _ in range(N):
    S, T, P = map(int, input().split())
    changes.append((S, P))
    changes.append((T, -P))

changes.sort()

water = 0
for t, p in changes:
    water += p
    if water > W:
        print('No')
        exit()
print('Yes')
