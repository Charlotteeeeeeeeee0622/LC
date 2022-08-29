class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        profit=0
        for right in range(0,len(prices)):
            #招最低点
            if prices[right]<prices[left]:
                left=right
            #找后面的最高点
            profit=max(profit,prices[right]-prices[left])
        return profit

        # while price[i]<price[j]:
#             if prices[i]>prices[i+1]:
#                 i+=1
#             if prices[j]<prices[j-1]:
#                 j-=1
