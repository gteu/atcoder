N = int(input())
trains = []
for _ in range(N - 1):
    trains.append(tuple(map(int, input().split())))

ans = []
for i in range(N):
    now = 0
    for j in range(i, N - 1):
        C, S, F = trains[j]
        if now < S:
            now = S
        else:
            now = ((now - 1) // F + 1) * F
        now += C
    ans.append(now)
print(*ans, sep='\n')
