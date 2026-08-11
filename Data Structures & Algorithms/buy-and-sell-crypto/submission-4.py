class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        l, r = 0, 1

        while r <= len(prices) - 1:
            provit = prices[r] - prices[l]

            if provit <= 0:
                l = r

            r += 1
                
            maxProfit = max(maxProfit, provit)

        return maxProfit        


