class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, max_profit, curr_profit, profit = 0, 0, 0, 0, 0
        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]
            if curr_profit < profit:
                buy = sell
                max_profit += profit
                profit = 0
            else:
                profit = curr_profit
            sell += 1
        max_profit += profit
        return max_profit
