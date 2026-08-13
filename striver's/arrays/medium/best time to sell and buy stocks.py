class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        max_profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right  # Jump to the new minimum price
            
            right += 1  # Move the selling day forward
            
        return max_profit

prices = [7, 1, 5, 3, 6, 4]
obj = Solution()
print(obj.maxProfit(prices))  # Output: 5 (Buy at 1, Sell at 6)
