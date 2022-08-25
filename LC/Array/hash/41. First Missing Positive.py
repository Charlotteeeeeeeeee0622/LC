"""
原地哈希就相当于，让每个数字n都回到下标为n-1的家里。
而那些没有回到家里的就成了孤魂野鬼流浪在外
他们要么是根本就没有自己的家（数字小于等于0或者大于nums.size()）
要么是自己的家被别人占领了（出现了重复）。
这些流浪汉被临时安置在下标为i的空房子里，之所以有空房子是因为房子i的主人i+1失踪了（数字i+1缺失）。
因此通过原地构建哈希让各个数字回家，我们就可以找到原始数组中重复的数字还有消失的数字。
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(nums, ind1, ind2):
            nums[ind1], nums[ind2] = nums[ind2], nums[ind1]

        l = len(nums)
        for i in range(l):
            # nums[i]值是不是在正常范围内，是不是位置没放对
            while 1 <= nums[i] <= l and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)

        for i in range(l):
            if i + 1 != nums[i]:
                return i + 1

        return l + 1
