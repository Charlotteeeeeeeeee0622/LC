# https://leetcode.com/problems/product-of-array-except-self/discuss/580519/Python-One-Pass-O(1)-Space-No-Division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
#         res[0]=1
#         prefix=nums[0]

#         res[1]=nums[0]
#         prefix=nums[0]*nums[1]

#         res[2]=nums[0]*nums[1]
#         prefix=nums[0]*nums[1]*nums[2]

#         -->res[len(nums)-1]=nums[0]*nums[1]*...*nums[len(nums)-2]

#         res[len(nums)-1]=1*res[len(nums)-1]
#         postfix=nums[len(nums)-1]*1

#         res[len(nums)-2]=nums[len(nums)-1]*res[len(nums)-2]
#         postfix=nums[len(nums)-2]*nums[]




n