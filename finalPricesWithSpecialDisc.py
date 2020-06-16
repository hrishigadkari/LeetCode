class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        j = i+1
        while i != len(prices):
            if j == len(prices):
                i += 1
                j = i + 1
            elif prices[i] >= prices[j]:
                prices[i] = prices[i] - prices[j]
                i = i+1
                j = i+1
            else:
                j += 1
        return prices
            
            
                