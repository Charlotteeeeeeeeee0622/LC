# ——————————————Solution1————————————————
# https://programmercarl.com/0034.%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E5%85%83%E7%B4%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%92%8C%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE.html#%E6%80%9D%E8%B7%AF
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 情况一：target 在数组范围的右边或者左边，例如数组{3, 4, 5}，target为2，或者数组{3, 4, 5},target为6，此时应该返回{-1, -1}
        # 情况二：target 在数组范围中，且数组中不存在target，例如数组{3,6,7},target为5，此时应该返回{-1, -1}
        # 情况三：target 在数组范围中，且数组中存在target，例如数组{3,6,7},target为6，此时应该返回{1, 1}
        def binarySearch(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:  # 不变量：左闭右闭区间
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            return -1

        index = binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        left, right = index, index
        while left - 1 >= 0 and nums[left - 1] == nums[left]:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == nums[right]:
            right += 1
        return [left, right]

# ——————————————Solution2————————————————
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                res.append(i)

        if not nums:
            return [-1, -1]

        if res == []:
            return [-1, -1]

        end = res[0]
        start = res.pop()

        return [start, end]




