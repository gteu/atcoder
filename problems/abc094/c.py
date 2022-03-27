N = int(input())
X = list(map(int, input().split()))

sX = sorted(X)
med1, med2 = sX[N // 2 - 1], sX[N // 2]
ans = []
for x in X:
    if x <= med1:
        ans.append(med2)
    else:
        ans.append(med1)
print(*ans, sep='\n')
