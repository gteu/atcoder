N = int(input())
used = set()
ans = 0
ans_i = -1
for i in range(N):
    S, T = input().split()
    T = int(T)
    if S not in used:
        if T > ans:
            ans_i = i
            ans = T
        used.add(S)
print(ans_i + 1)
