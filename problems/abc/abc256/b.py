N = int(input())
A = list(map(int, input().split()))
B = [0, 0, 0, 0]
ans = 0
for a in A:
    new_B = [0, 0, 0, 0]
    B[0] += 1
    for i in range(4):
        if i + a < 4:
            new_B[i + a] += B[i]
        else:
            ans += B[i]
    B = new_B
print(ans)
