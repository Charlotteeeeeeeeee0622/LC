class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq>len(nums)//2
        # res.append
        res = []
        nf = collections.defaultdict(int)
        for n in nums:
            nf[n] += 1
        # nf=sorted(nf.items(),key=lambda x:x[1],reverse=True)
        for i, f in nf.items():
            if f > len(nums) // 2:
                res = i
        return res

    # 投票算法
    def majorityElement(self, nums):
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate