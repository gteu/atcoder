N = int(input())
town = []
for _ in range(N):
    town.append(tuple(map(int, input().split())))

town.sort(key=lambda x: x[0] * 2 + x[1], reverse=True)

cur_a = sum([a for a, b in town])
cur_b = 0
for i, (a, b) in enumerate(town):
    cur_a -= a
    cur_b += a + b
    if cur_b > cur_a:
        print(i + 1)
        exit()
