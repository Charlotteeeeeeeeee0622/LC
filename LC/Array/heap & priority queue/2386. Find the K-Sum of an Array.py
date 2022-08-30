"""从最大的子序列和来考虑，那么这个序列和就是所有正数的和 sum。
怎么找到第二大的子序列和？从最大的子序列和中减去最小的正数或加上最大的负数。
为了统一操作，将负数取反，然后排序，每次取最小的数，得到的就是最小的正数或最大的负数。sum 中减去它，就可以得到下一个更小的子序列和。
被减去的数们实际上也是组成了一个子序列。按照生成子序列的模板，就是依次对每个数，考虑选择它，还是不选择它。
这样分析之后，就可以回答大家的两个问题：

Q：怎么保证 pq 的顶就是答案？A：因为是用当前值最大和减去最小值，所以得到的一定是下一个略小的最大和。
Q：保留和不保留 nums[i-1] 是不是写反了？A：是否保留指的是在被 *减去* 的子序列中是否保留此数。所以，如果不保留的话，反而是要加回来，因为它不该被从 sum 里减去。
"""
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        # 最大值
        m = sum(x for x in nums if x > 0)
        pq = [(-m, 0)]
        vals = sorted(abs(x) for x in nums)
        for _ in range(k):
            x, i = heappop(pq)
            if i < len(vals):
                heappush(pq, (x+vals[i], i+1)) # 保留 nums[i-1]
                if i: heappush(pq, (x-vals[i-1]+vals[i], i+1)) # 不保留 nums[i-1]
        return -x