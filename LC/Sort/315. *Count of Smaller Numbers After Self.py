# https://leetcode.cn/problems/count-of-smaller-numbers-after-self/solution/gui-bing-pai-xu-suo-yin-shu-zu-python-dai-ma-java-/
class Solution:

    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        if len(nums) == 1:
            return [0]
        self.ans = [0] * len(nums)
        temp = []
        for index, value in enumerate(nums):
            temp.append((value, index))
        nums = temp
        self.merge_sort(nums)
        return self.ans

    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                res.append(left[i])
                self.ans[left[i][1]] += j
                i += 1

            else:
                res.append(right[j])
                j += 1
        if i == len(left):
            res += right[j:]
        else:
            for k in range(i, len(left)):
                self.ans[left[k][1]] += j
            res += left[i:]
        return res