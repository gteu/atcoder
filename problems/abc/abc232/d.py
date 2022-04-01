H, W = map(int, input().split())
C = []
for i in range(H):
    C.append(input())
visited = [[False] * W for _ in range(H)]

stack = [(0, 0, 1)]
max_d = -1
while stack:
    i, j, d = stack.pop()
    visited[i][j] = True
    max_d = max(d, max_d)
    if i + 1 < H and C[i+1][j] == "." and not visited[i+1][j]:
        stack.append((i+1, j, d+1))
    if j + 1 < W and C[i][j+1] == "." and not visited[i][j+1]:
        stack.append((i, j+1, d+1))
print(max_d)