from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val, max_val = 1, 0
        for pile in piles:
            if min_val > pile:
                min_val = pile
            if max_val < pile:
                max_val = pile
        while min_val <= max_val:
            mid = (min_val + max_val) // 2
            if self.check_pile(piles, mid, h):
                max_val = mid - 1
                last_true = mid
            else:
                min_val = mid + 1

        return last_true

    def check_pile(self, piles, k, h):
        res = 0
        for pile in piles:
            res += ceil(pile / k)
            if res > h:
                return False
        return True


r = Solution()
print(r.minEatingSpeed(piles=[3, 6, 7, 11], h=8), 'res = 4')
print(r.minEatingSpeed(piles=[312884470], h=312884469), 'res = 2')
