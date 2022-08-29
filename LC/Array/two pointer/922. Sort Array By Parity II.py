class Solution:
    def sortArrayByParityII(self, nums):
        i, j, n = 0, 1, len(nums)
        while j < n and i < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums