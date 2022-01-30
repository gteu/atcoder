s = input()

def is_kaibun(s):
    flag = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            flag = False
            break
    return flag

l_i, r_i = 0, 0
for i in range(len(s)):
    flag = True
    if s[i] != 'a':
        flag = False
    if not flag:
        s = s[i:]
        l_i = i
        break

n = len(s)
for i in reversed(range(len(s))):
    flag = True
    if s[i] != 'a':
        flag = False
    if not flag:
        s = s[:i+1]
        r_i = n - i - 1
        break
if l_i > r_i:
    print("No")
    exit()

if is_kaibun(s):
    print("Yes")
else:
    print("No")