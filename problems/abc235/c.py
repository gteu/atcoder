n, q = map(int, input().split())
A = list(map(int, input().split()))
count = {}

for i, a in enumerate(A):
    if count.get(a):
        count[a].append(i+1)
    else:
        count[a] = [i+1]

for i in range(q):
    x, k = map(int, input().split())
    if count.get(x) and len(count[x]) >= k:
        print(count[x][k-1])
    else:
        print(-1)