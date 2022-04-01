N = int(input())
T = []
for i in range(5):
    T.append(int(input()))

min_t = min(T)
print((N - 1) // min_t + 5)
