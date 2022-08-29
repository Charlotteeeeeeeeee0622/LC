#mhttps://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        for right in range(len(nums)):
            k-=1-nums[right]
            if k<0:
                k+=1-nums[left]
                left+=1
        return right-left+1

# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         left=0
#         right=1
#         nsum=0
#         while right<len(nums):
#             nsum=max(nsum,right-left)
#             while nums[right]==1:
#                 right+=1
#             while nums[right]==0:
#                 k-=1
#                 right+=1
#             right+=1
#         return nsum


