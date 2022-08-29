# ——————————————Solution1————————————————
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1: return False
        target //= 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for nsum in range(target, num - 1, -1):
                # dp[nsum-num],即总容量只剩nsum-num
                # dp[nsum]要想为True要有存在dp[nsum-num]为True
                # dp[nsum]初始值是False
                # nsum-num为True说明，nsum=num,或这nsum为num以及更前面数组元素和
                dp[nsum] = dp[nsum] or dp[nsum - num]
        return dp[target]


# ——————————————Solution2————————————————
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum & 1:
            return False
        target = sum // 2
        n = len(nums)

        dp = [False for _ in range(target + 1)]

        # 依据状态定义做判断:
        # 因为下标[0,0]中nums[0]凑不出0所以设置成False
        # 如果依据状态转移则可以理解为:
        # [j - nums[i]] == 0 表示nums[i]恰好为一组,其余为一组,刚才凑成,所以True没问题
        dp[0] = True

        # 先填表格第 0 行，第 1 个数只能让容积为它自己的背包恰好装满
        if nums[0] <= target:
            dp[nums[0]] = True

        for i in range(1, n):
            for j in range(target, -1, -1):
                # 「从后向前」 写的过程中，一旦 nums[i] <= j 不满足，可以马上退出当前循环
                # 因为后面的 j 的值肯定越来越小，没有必要继续做判断，直接进入外层循环的下一层。
                # 相当于也是一个剪枝，这一点是「从前向后」填表所不具备的。
                if nums[i] <= j:
                    # j 装得下，j-nums[i]也装得下
                    dp[j] = dp[j] or dp[j - nums[i]]
                else:
                    break
        return dp[-1]

