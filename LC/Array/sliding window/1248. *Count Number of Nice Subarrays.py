# https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-O(1)-Space
# It appears that what you mean by atMost
# is the number of subarrays where count of odd numbers is greater than 0 and less than equal to k.
# By subtracting atMost(A, k-1),
# you are effectively removing all subarrays
# with count of odd numbers greater than 0 and less than or equal to k-1
# thereby giving you all subarrays which have number of odd numbers exactly equal to k.
# Interesting approach, thanks for sharing.
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            res=0
            left=0
            for right in range(len(nums)):
                k-=nums[right]%2
                while k<0:
                    k+=nums[left]%2
                    left+=1
                # 长度累加
                res+=right-left+1
            return res
        return atmost(k)-atmost(k-1)