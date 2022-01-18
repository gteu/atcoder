import math

X = input()

for i in range(len(X), 19):
    for j in range(1, 10):
        for k in range(1, 10):
            if j > k and math.floor(j/(j-k)) + 1 >= i:
                ans = "".join(map(str, [l for l in range(j, -1, k-j)][:i]))
                if int(ans) >= int(X):
                    print(ans)
                    exit()
            elif j == k:
                ans = str(j) * i
                if int(ans) >= int(X):
                    print(ans)
                    exit()
            elif j < k and math.floor((9-j)/(k-j)) + 1 >= i:
                ans = "".join(map(str, [l for l in range(j, 10, k-j)][:i]))
                if int(ans) >= int(X):
                    print(ans)
                    exit()