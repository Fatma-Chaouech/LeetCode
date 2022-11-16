class Solution:
    def search(self, nums: List[int], target: int) -> int:
           
        last_el = len(nums)-1
        first_el = 0
        while(last_el - first_el >= 0):
            middle_index = first_el + ((last_el - first_el)//2)
            middle_element = nums[middle_index]
            
            if middle_element == target:
                return middle_index
            elif middle_element < target : 
                first_el = middle_index + 1
            else :
                last_el = middle_index - 1
                
        return -1
            
    