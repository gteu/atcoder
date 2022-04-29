N = int(input())
used = set()
for i in range(1, N + 1):
    S = input()
    if S not in used:
        print(i)
        used.add(S)
