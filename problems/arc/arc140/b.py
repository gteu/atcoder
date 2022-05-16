from collections import deque
from bisect import bisect_left
N = int(input())
S = input()
splits = S.split('ARC')
ans = 0
nums = []
for sp, sc in zip(splits, splits[1:]):
    cnt_a = 0
    for c in sp[::-1]:
        if c == 'A':
            cnt_a += 1
        else:
            break
    cnt_c = 0
    for c in sc:
        if c == 'C':
            cnt_c += 1
        else:
            break
    nums.append(min(cnt_a, cnt_c))
nums.sort()
nums = deque(nums)
is_odd = 1
while nums:
    i = bisect_left(nums, nums[-1])
    if is_odd:
        if nums[i] > 0:
            nums[i] -= 1
        else:
            nums.pop()
    else:
        nums.popleft()
    is_odd = 1 - is_odd
    ans += 1
print(ans)
