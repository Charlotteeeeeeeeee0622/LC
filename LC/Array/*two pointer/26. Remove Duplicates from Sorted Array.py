class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for fast in range(len(nums) - 1):
            if nums[fast] != nums[fast + 1]:
                nums[slow] = nums[fast + 1]
                slow += 1
        return slow
