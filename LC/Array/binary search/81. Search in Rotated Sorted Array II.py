class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0;
        r = len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if target == nums[mid]:
                return True

            elif nums[mid] == nums[l]:
                l += 1

            elif nums[mid] == nums[r]:
                r -= 1

            elif nums[mid] > nums[l]:
                if target <= nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if target > nums[mid] and target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

