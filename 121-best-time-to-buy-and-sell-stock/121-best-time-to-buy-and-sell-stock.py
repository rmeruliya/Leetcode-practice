class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        l = 0
        
        for i in range(1,len(prices)):
            if prices[i] < prices[l]:
                l = i
            maxi = max(maxi,prices[i] - prices[l])
        return maxi