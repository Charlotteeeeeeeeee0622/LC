class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        # base case
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            # to calculate rob the previous one or not, which higher
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])

        return dp[len(nums)]