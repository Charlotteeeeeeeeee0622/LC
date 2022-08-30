import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num=[-n for n in nums]
        heapq.heapify(num)
        res=[]
        for i in range(k):
            x=heapq.heappop(num)
            res.append(x)
        return -res[-1]