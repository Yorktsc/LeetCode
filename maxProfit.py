class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0] + [-1] * (len(prices) - 1)
        l_price, l_index = prices[0], 0
        for i, price in enumerate(prices):
            if i == 0:
                continue
            if price < l_price:
                l_price = price
                l_index = i
                dp[i] = 0
            else:
                dp[i] = max((price - l_price) + dp[l_index], 0)
        return max(dp)
