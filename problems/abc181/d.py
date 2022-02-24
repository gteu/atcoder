from collections import Counter
s = input()
ct = Counter(s)
if len(s) <= 2:
    print('Yes' if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0 else 'No')
else:
    for i in range(0, 1000, 8):
        ct_tmp = Counter(str(i).zfill(3))
        flag = True
        for k, v in ct_tmp.items():
            if ct_tmp[k] > ct[k]:
                flag = False
        if flag:
            print('Yes')
            exit()
    print('No')
