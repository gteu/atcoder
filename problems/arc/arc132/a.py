n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))
q = int(input())
for i in range(q):
    r, c = map(int, input().split())
    print('#' if R[r-1] + C[c-1] > n else '.', end='')