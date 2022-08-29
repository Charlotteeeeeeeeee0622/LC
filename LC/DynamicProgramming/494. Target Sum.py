# ——————————————Solution1————————————————
# https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.
# DFS思路
class Solution:

    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        return self.dp(nums, S, index, curr_sum)

    def dp(self, nums, target, index, curr_sum):
        # Base Cases
        if index < 0 and curr_sum == target:
         return 1
        if index < 0:
         return 0

        # Decisions
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index])

        return positive + negative

# ——————————————Solution2————————————————
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumValue=sum(nums)
        if abs(target)>sumValue or (sumValue+target)%2==1:
            return 0
        # 负数组数字和正数组数字之和为sum
        # neg+pos=sum
        # 正数组减去负数组为target
        # pos-(sum-pos)=target
        # 2*pos-sum=target
        # pos=(target+sum)/2
        pos=(sumValue+target)//2
        dp=[0]*(pos+1)
        dp[0]=1
        for num in nums:
            for i in range(pos,num-1,-1):
                # dp[j]表示填满和为pos有这么多种方法
                dp[i]+=dp[i-num]
        return dp[pos]