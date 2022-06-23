N, M = map(int, input().split())
price = []
for _ in range(N):
    A, B = map(int, input().split())
    price.append((A, B))
price.sort()
ans = 0
for a, b in price:
    ans += min(b, M) * a
    M -= min(b, M)
print(ans)
