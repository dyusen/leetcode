from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (end + start) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_list = matrix[mid]
                break
            elif matrix[mid][0] > target:
                end = mid - 1
            elif matrix[mid][-1] < target:

                start = mid + 1
        else:
            return False

        start = 0
        end = len(target_list) - 1

        while start <= end:
            mid = (end + start) // 2
            if target_list[mid] == target:
                return True
            elif target_list[mid] > target:
                end = mid - 1
            elif target_list[mid] < target:
                start = mid + 1

        return False
