K = int(input())
cur = 0
for i in range(10 ** 6 + 2):
    cur = (10 * cur + 7) % K
    if cur % K == 0:
        print(i + 1)
        exit()
print(-1)
