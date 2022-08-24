# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        # 从后往前找
        # 找到最低点
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -= 1
# 1.我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。
#   因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。
#   比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
# 2.我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：
#   在尽可能靠右的低位进行交换，需要从后向前查找
#   将一个 尽可能小的「大数」 与前面的「小数」交换。
#   比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
# 3.将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。
#   以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；
#   然后需要将 5 之后的数重置为升序，得到 123546。
#   显然 123546 比 123564 更小，123546 就是 123465 的下一个排列.
