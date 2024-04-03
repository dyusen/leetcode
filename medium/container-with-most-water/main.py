from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            candidate = (r - l) * min(height[l], height[r])
            if res < candidate:
                res = candidate

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return res


r = Solution()
print(r.maxArea(height=[1, 100, 6, 2, 100, 4, 8, 3, 7]))
