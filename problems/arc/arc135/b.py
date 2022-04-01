N = int(input())
S = list(map(int, input().split()))

x = [0, 0]
for s in S:
    x.append(s - x[-1] - x[-2])
print(x)
c1 = -min(x[::3])
c2 = -min(x[1::3])
c3 = min(x[2::3])
if c1 + c2 > c3:
    print("No")
else:
    ans = [c1, c2]
    for s in S:
        ans.append(s - ans[-1] - ans[-2])
    print("Yes")
    print(*ans)
