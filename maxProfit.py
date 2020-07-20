class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        add = 0
        for i in range(1,len(prices)):
            if prices[i]-prices[i-1]>0:
                add += prices[i]-prices[i-1]
        return add