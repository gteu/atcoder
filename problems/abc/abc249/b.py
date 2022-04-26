S = input()
used = set()
up, low = False, False
for s in S:
    if s.isupper():
        up = True
    if s.islower():
        low = True
    if s in used:
        print('No')
        exit()
    used.add(s)

if up and low:
    print('Yes')
else:
    print('No')
