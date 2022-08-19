class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            if len(path) >= 2:
                # make list to tuple to make it hashable(add to a set)
                res.add(tuple(path))
            for i in range(len(nums)):
                # try to add the first
                # want to make sure that nums[i]>=last add
                if not path or path[-1] <= nums[i]:
                    dfs(nums[i + 1:], path + [nums[i]])

        res = set()
        dfs(nums, [])
        return res