class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        el_dict = {')': '(', ']' : '[', '}':'{'}
        for char in s:
          
            if char in el_dict.values():
                stack.append(char)
            elif len(stack) == 0 or el_dict[char] != stack[-1] :
                return False
            else: 
                stack.pop()
        
        if len(stack) > 0:
            return False
        
        return True
            
        