class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, max_profit, curr_profit = 0, 1, 0, 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                curr_profit = prices[sell] - prices[buy]
            if max_profit < curr_profit:
                max_profit = curr_profit
            sell += 1
        return max_profit
