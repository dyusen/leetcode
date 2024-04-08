from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            if nums[l] > nums[r]:
                if nums[mid] > nums[l] and nums[mid] > nums[r]:  # разрыв справа
                    if target >= nums[l] and target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:  # разрыв слева
                    if target > nums[mid] and target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
            else:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


r = Solution()
print(r.search(nums=[4, 5, 6, 7, 0, 1, 2], target=6), "2")
print(r.search(nums=[4, 5, 6, 7, 0, 1, 2], target=1), "5")

print(r.search(nums=[0, 1, 2, 3, 4, 5, 6, 7, ], target=1), "1")
print(r.search(nums=[6, 7, 0, 1, 2, 3, 4, 5], target=1), "3")
print(r.search(nums=[3, 1], target=1), "1")
print(r.search(nums=[1, 3], target=1), "0")
