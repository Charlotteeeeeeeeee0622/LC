# ——————————————Solution1————————————————
# 别人的快速版
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


# ——————————————Solution2————————————————
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0, nums.pop())
            k -= 1

# ——————————————Solution3————————————————
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # 1.翻转整个数组
        self.reverse(nums, 0, n - 1)
        # 2.翻转前k个元素
        self.reverse(nums, 0, k - 1)
        # 3.翻转k后面的元素
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1