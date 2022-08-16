class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, path):
            if not nums:
                res.append(path)
                # 没有return，不要回溯

            for i in range(len(nums)):
                backtracking(nums[:i] + nums[i + 1:], path + [nums[i]])

        res = []
        backtracking(nums, [])
        return res