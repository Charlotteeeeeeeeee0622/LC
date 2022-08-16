class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, path):
            res.append(path)

            for i in range(len(nums)):
                backtracking(nums[i + 1:], path + [nums[i]])

        res = []
        backtracking(nums, [])
        return res
