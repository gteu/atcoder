N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

com = len(set(A) & set(B))
cnt = 0
for i in range(N):
    if A[i] == B[i]:
        cnt += 1
print(cnt)
print(com - cnt)
