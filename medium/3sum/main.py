from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == a:
                continue

            l = i + 1
            r = len(nums) - 1
            target = -a
            while l < r:
                candidate = nums[l] + nums[r]
                if candidate > target:
                    r -= 1
                elif candidate < target:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


r = Solution()
print(r.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(r.threeSum(nums=[1, 2, -2, -1]))
print(r.threeSum(nums=[0, 0, 0, 0]))
print(r.threeSum(nums=[-2, 0, 1, 1, 2]))
print(r.threeSum(nums=[-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
print([[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1]])
