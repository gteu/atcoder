N, X = map(int, input().split())
vis = {0}
for _ in range(N):
    a, b = map(int, input().split())
    new = set()
    for v in vis:
        new.add((v+a))
        new.add((v+b))
    vis = new

if X in vis:
    print('Yes')
else:
    print('No')
