class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pmax = 1
        pmin = 1

        res = -float('inf')

        for i in range(len(nums)):
            if nums[i] < 0:
                pmax, pmin = pmin, pmax

            pmax = max(nums[i], nums[i] * pmax)
            pmin = min(nums[i], nums[i] * pmin)

            res = max(pmax, res)

        return res
