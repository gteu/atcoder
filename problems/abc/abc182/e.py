H, W, N, M = map(int, input().split())
lamps = [[0] * W for _ in range(H)]
blocks = [[0] * W for _ in range(H)]
lights = [[0] * W for _ in range(H)]
for _ in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    lamps[a][b] = 1
for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    blocks[c][d] = 1

for i in range(H):
    light = 0
    for j in range(W):
        if lamps[i][j]:
            light = 1
        if blocks[i][j]:
            light = 0
        if light:
            lights[i][j] = 1

    light = 0
    for j in reversed(range(W)):
        if lamps[i][j]:
            light = 1
        if blocks[i][j]:
            light = 0
        if light:
            lights[i][j] = 1


for j in range(W):
    light = 0
    for i in range(H):
        if lamps[i][j]:
            light = 1
        if blocks[i][j]:
            light = 0
        if light:
            lights[i][j] = 1

    light = 0
    for i in reversed(range(H)):
        if lamps[i][j]:
            light = 1
        if blocks[i][j]:
            light = 0
        if light:
            lights[i][j] = 1


ans = sum([sum(light) for light in lights])
print(ans)
