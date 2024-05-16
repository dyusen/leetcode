from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max = 0
        slow, fast = 0, 1
        while fast < len(prices) - 1:
            if prices[fast] > prices[slow]:
                profit = prices[fast] - prices[slow]
                current_max = max(current_max, profit)
            else:
                slow = fast
            fast += 1

        return current_max


r = Solution()
print(r.maxProfit(prices=[7, 1, 5, 3, 6, 4]), 5)
