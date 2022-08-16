class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, path):

            res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtracking(nums[i + 1:], path + [nums[i]])

        res = []
        backtracking(sorted(nums), [])
        return res