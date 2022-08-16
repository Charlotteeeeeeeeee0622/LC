class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('INF')
        nsum = 0
        j = 0

        for i in range(len(nums)):
            # 给sum赋初值
            nsum += nums[i]
            while nsum >= target:
                # 长度最小值的比较，右边界i，左边界j
                res = min(res, i - j + 1)
                nsum -= nums[j]
                j += 1

        return 0 if res == float('INF') else res

        