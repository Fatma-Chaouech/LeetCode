class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)) :
            current_element = nums[i]
            needed_value = target - current_element
            indices = [j for j, x in enumerate(nums) if x == needed_value and j != i]
            if len(indices) > 0:
                result = indices[0]
                return list((i, result))
