def solve(t, k):
    if t == 0:
        return S[k - 1]
    nums = [k]
    while t > 0 and k > 1:
        k = (k - 1) // 2 + 1
        t -= 1
        nums.append(k)
    nums.reverse()

    cur = S[nums[0] - 1]
    cur = ref[(ref.index(cur) + t) % 3]
    for p, c in zip(nums, nums[1:]):
        if p * 2 == c + 1:
            cur = ref[(ref.index(cur) + 1) % 3]
        else:
            cur = ref[(ref.index(cur) + 2) % 3]

    return cur


S = input()
Q = int(input())
ans = []
ref = ['A', 'B', 'C']
for _ in range(Q):
    t, k = map(int, input().split())
    ans.append(solve(t, k))
print(*ans, sep='\n')
