N = int(input())
A = list(map(int, input().split()))
acc = 0
acc_max = 0
ans = 0
s = 0
for a in A:
    acc += a
    acc_max = max(acc_max, acc)
    ans = max(ans, s + acc_max)
    s += acc
print(ans)
