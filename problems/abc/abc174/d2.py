N = int(input())
C = input()
wc = C.count('W')
print(C[N - wc:].count('R'))
