from bisect import bisect_left, bisect_right, insort_left, insort_right

a = [1,2,3,3,5,7,7,7]

bisect_left(a, 3)
# → 2

bisect_right(a, 3)
# → 4

insort_left(a, 3) # 参照渡しでaが置き換わる。
# → [1,2,3,3,3,5,7,7,7]


# example 1)
# 5以上の値の数を求めるとき
ans = len(a) - bisect_left(a, 5)

# example 2)
# 5より大きい値の数を求めるとき
ans = len(a) - bisect_right(a, 5)