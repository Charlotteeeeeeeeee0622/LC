class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, path):
            if len(path) >= 2:
                res.add(tuple(path))
            for i in range(len(nums)):
                if not path or path[-1] <= nums[i]:
                    backtracking(nums[i + 1:], path + [nums[i]])

        res = set()
        backtracking(nums, [])
        return res
