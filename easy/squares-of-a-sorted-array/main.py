from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = []
        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res.append(nums[l] ** 2)
                l += 1
            else:
                res.append(nums[r] ** 2)
                r -= 1

        return res[::-1]


r = Solution()

print(r.sortedSquares([-2, 0, 1, 2, 3]))
print(r.sortedSquares([-3, -2, -1, 0, 1]))
print(r.sortedSquares([-3]))