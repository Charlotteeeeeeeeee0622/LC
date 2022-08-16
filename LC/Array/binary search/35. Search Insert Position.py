# https://programmercarl.com/0035.%E6%90%9C%E7%B4%A2%E6%8F%92%E5%85%A5%E4%BD%8D%E7%BD%AE.html#%E6%80%9D%E8%B7%AF
# https://leetcode.com/problems/search-insert-position/discuss/249092/Come-on-forget-the-binary-search-patterntemplate!-Try-understand-it!
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # // 分别处理如下三种情况
        # // 目标值在数组所有元素之前
        # // 目标值等于数组中某一个元素
        # // 目标值插入数组中的位置
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2#在左闭右闭的区间里寻找
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
        return right+1