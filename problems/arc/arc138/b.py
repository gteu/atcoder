from collections import deque
N = int(input())
A = deque(list(map(int, input().split())))

b = 0
while A:
    if A[-1] == b:
        A.pop()
    else:
        if A[0] == b ^ 1:
            print('No')
            exit()
        A.popleft()
        b ^= 1
print('Yes')
