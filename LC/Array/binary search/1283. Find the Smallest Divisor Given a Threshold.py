class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left=1
        right=max(nums)
        #很方便，最后返回ans,找不到就是-1
        ans=-1
        #why
        while left<=right:
            mid=left+(right-left)//2
            totalsum=0
            for i in nums:
                 totalsum+=(i-1)//mid+1
            #totalsum = sum((x - 1) // mid + 1 for x in nums)
            if totalsum<=threshold:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans