import math 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_total = math.inf, 0

        for price in prices:
            min_price = min(min_price, price)
            max_total = max(max_total, price - min_price)

        return max_total