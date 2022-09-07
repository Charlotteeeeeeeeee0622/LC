class Solution:
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        # dp[i][0] : max length of subarray ending with index i With positive product
        # dp[i][1] : max length of subarray ending with index i With negative product

        # Base case: when index is 0, only one number can be used
        if nums[0] > 0:
            dp[0][0] = 1

        if nums[0] < 0:
            dp[0][1] = 1

        res = dp[0][0]

        for i in range(1, n):
            cur = nums[i]

            if cur > 0:
                dp[i][0] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0:  # if previous negative subarray exists
                    dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)
            if cur < 0:
                dp[i][1] = dp[i - 1][0] + 1
                if dp[i - 1][1] > 0:  # if previous negative subarray exists
                    dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)

            res = max(res, dp[i][0])

        return res