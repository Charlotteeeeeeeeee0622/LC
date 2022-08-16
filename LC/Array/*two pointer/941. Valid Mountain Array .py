# ——————————————Solution1————————————————
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left = 0
        right = len(arr) - 1

        if len(arr) <= 2:
            return False

        while left < right and left > 0:
            if not nums[left] > nums[left - 1] and not nums[right - 1] > nums[right]:
                return False

        return True


# ——————————————Solution2————————————————
class Solution:
    def validMountainArray(self, arr):
        i, j, n = 0, len(arr) - 1, len(arr)
        while i + 1 < n and arr[i] < arr[i + 1]: i += 1
        while j > 0 and arr[j - 1] > arr[j]: j -= 1
        return 0 < i == j < n - 1


# ——————————————Solution3————————————————
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        end=len(arr)-1
        start=0
        while start<len(arr)-1 and arr[start+1]>arr[start]:
            start+=1
        while end>0 and arr[end-1]>arr[end]:
            end-=1
        if end==start and end!=len(arr)-1 and start!=0:
            return True
        else:
            return False

# See other mountain array problems:
# 845. Longest Mountain in Array:
# https://leetcode.com/problems/longest-mountain-in-array/discuss/937652/Python-one-pass-O(1)-space-explained
#
# 1671 Minimum Number of Removals to Make Mountain Array:
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/discuss/952053/Python-3-solutions%3A-LIS-dp-O(n-log-n)-explained
#
