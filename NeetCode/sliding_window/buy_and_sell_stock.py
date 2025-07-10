#
# diff: ez
# sol: optimal
#   time complex | O(n)
#   space complex | O(1)
#   time | 00:16:16.34
# 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        pointer_l = 0
        pointer_r = 1
        while pointer_r < len(prices):
            if prices[pointer_l] < prices[pointer_r]:
                temp = prices[pointer_r] - prices[pointer_l]
                if temp > max_profit:
                    max_profit = temp
            else:
                pointer_l = pointer_r
            pointer_r += 1
        return max_profit