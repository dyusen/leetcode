class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow_pointer = 0

        while slow_pointer < len(numbers) - 1:
            high = len(numbers) - 1
            low = slow_pointer + 1
            second_target = target - numbers[slow_pointer]

            while low <= high:
                mid = (high + low) // 2
                if numbers[mid] < second_target:
                    low = mid + 1
                elif numbers[mid] > second_target:
                    high = mid - 1
                else:
                    return [slow_pointer + 1, mid + 1]
            slow_pointer += 1
