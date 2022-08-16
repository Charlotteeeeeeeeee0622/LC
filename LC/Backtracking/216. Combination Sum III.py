# https://leetcode.com/problems/combination-sum-iii/discuss/60805/Easy-to-understand-Python-solution-(backtracking).
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracking(nums, k, target, path):
            if k < 0 or target < 0:
                return
            if k == 0 and target == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                backtracking(nums[i + 1:], k - 1, target - nums[i], path + [nums[i]])

        res = []
        backtracking(list(range(1, 10)), k, n, [])
        return res