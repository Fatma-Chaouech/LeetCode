class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            sum_ = numbers[start] + numbers[end]
            if sum_ > target:
                end -= 1
            elif sum_ < target:
                start += 1
            else:
                return [start + 1, end + 1]
