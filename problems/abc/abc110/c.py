S = input()
T = input()
convert = [-1] * 26
t_used = set()
for i in range(len(S)):
    s = ord(S[i]) - ord('a')
    t = ord(T[i]) - ord('a')
    if convert[s] == -1 and t not in t_used:
        convert[s] = t
        t_used.add(t)
    elif convert[s] != t:
        print('No')
        exit()
print('Yes')
