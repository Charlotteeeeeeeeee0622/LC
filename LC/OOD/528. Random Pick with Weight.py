class Solution:

    def __init__(self, w: List[int]):
        self.dp=[0]*len(w)
        for i in range(len(w)):
            self.dp[i]=self.dp[i-1]+w[i]

    def pickIndex(self) -> int:
        radint=random.randint(1,self.dp[-1])
        l,r=0,len(self.dp)-1
        while l<r:
            mid=(l+r)//2
            if self.dp[mid]>=radint:
                r=mid
            else:
                l=mid+1
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()