S = input()
T = input()

MOD = 26
k = ord(T[0]) - ord(S[0])
for i in range(len(S)):
    if k % MOD != (ord(T[i]) - ord(S[i])) % MOD:
        print("No")
        exit()
print("Yes")
