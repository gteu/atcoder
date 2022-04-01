N = int(input())
sums = []
difs = []
for _ in range(N):
    x, y = map(int, input().split())
    sums.append(x + y)
    difs.append(x - y)
print(max(max(sums) - min(sums), max(difs) - min(difs)))
