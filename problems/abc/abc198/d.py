from itertools import permutations


def s_to_key(s):
    ret = []
    for c in s:
        ret.append(unique.index(c))
    return ret


s1 = input()
s2 = input()
s3 = input()
unique = set(s1 + s2 + s3)
if len(unique) > 10:
    print('UNSOLVABLE')
    exit()
unique = list(unique)
s1_k = s_to_key(s1)
s2_k = s_to_key(s2)
s3_k = s_to_key(s3)

for nums in permutations(range(10), len(unique)):
    n1 = int(''.join(([str(nums[k]) for k in s1_k])))
    n2 = int(''.join(([str(nums[k]) for k in s2_k])))
    n3 = int(''.join(([str(nums[k]) for k in s3_k])))
    if n1 + n2 == n3 and len(str(n1)) == len(s1) and len(str(n2)) == len(s2) and len(str(n3)) == len(s3) and n1 > 0 and n2 > 0 and n3 > 0:
        print(n1)
        print(n2)
        print(n3)
        exit()
print('UNSOLVABLE')
