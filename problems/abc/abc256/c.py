h1, h2, h3, w1, w2, w3 = map(int, input().split())
ans = 0
for i in range(1, 30):
    for j in range(1, 30):
        for k in range(1, 30):
            for l in range(1, 30):
                if i + j < h1 and i + k < w1 and k + l < h2 and j + l < w2:
                    v1 = w3 - h1 - h2 + i + j + k + l
                    v2 = h3 - w1 - w2 + i + j + k + l
                    if v1 > 0 and v1 == v2:
                        ans += 1
print(ans)
