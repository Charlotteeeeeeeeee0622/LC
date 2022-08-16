class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(nums, k, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(len(nums)):
                backtracking(nums[i + 1:], k, path + [nums[i]])

        res = []
        nums = list(range(1, n + 1))
        backtracking(nums, k, [])
        return res