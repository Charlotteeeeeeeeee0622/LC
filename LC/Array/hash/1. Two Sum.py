class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [i, prev[diff]]

            prev[n] = i