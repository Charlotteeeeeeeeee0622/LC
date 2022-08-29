class Solution:
    def rob(self, nums: [int]) -> int:
        # 难道在前 n 间的最高金额 dp[n]情况下，第 n 间一定被偷了吗？
        # 假设没有被偷那 n+1 间的最大值应该也可能是 dp[n+1] = dp[n] + num 吧？
        # 其实这种假设的情况可以被省略，这是因为：
        # 假设第 n 间没有被偷
        # 那么此时 dp[n] = dp[n-1]
        # 此时 dp[n+1] = dp[n] + num = dp[n-1] + num
        # 即可以将 两种情况合并为一种情况 考虑；
        # 假设第 n 间被偷
        # 那么此时 dp[n+1] = dp[n] + num 不可取
        # 因为偷了第 n 间就不能偷第 n+1 间

        dp1 = {}
        n = len(nums)
        if n == 1:
            return nums[0]
        # 不偷第一家

        dp1[0] = 0
        dp1[-1] = 0

        for i in range(1, n):
            dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])

        # 不偷最后一家
        dp2 = {}
        dp2[0]=nums[0]
        dp2[-1] = 0
        for i in range(1, n - 1):
            dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])

        return max(dp1[n - 1], dp2[n - 2])

#         dp1=[0]*(len(nums)+1)
#         dp2=[0]*(len(nums)+1)

#         dp1[0]=dp2[0]=0
#         dp1[1]=dp2[1]=nums[0]
#         dp1[2]=dp2[2]=0
#         dp1[3]=dp2[3]=max(nums[:3])

#         for i in range(4,len(nums)-1):
#             dp1[i]=max(dp1[i-2]+nums[i-1],dp1[i-1])

#         for i in range(5,len(nums)):
#             dp2[i]=max(dp2[i-2]+nums[i-1],dp2[i-1])

#         return max(dp1[len(nums)],dp2[len(nums)-1]) if len(nums)!=1 else nums[0]