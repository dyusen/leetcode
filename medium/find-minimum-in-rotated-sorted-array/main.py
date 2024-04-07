from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        current_min = nums[0]
        while l < r:
            mid = (l + r) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] >= nums[r]:
                l = mid + 1
                current_min = nums[r]
            else:
                r = mid - 1
                current_min = nums[l]
        return current_min


r = Solution()
print("res: 1 /", r.findMin([3, 4, 5, 1, 2]))
print("res: 0 /", r.findMin([4, 5, 6, 7, 0, 1, 2]))
print("res: 11 /", r.findMin([11, 12, 13, 14]))
print("res: 1 /", r.findMin([2, 1]))
print("res: 1 /", r.findMin([3, 1, 2]))
