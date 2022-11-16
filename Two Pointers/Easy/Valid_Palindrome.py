class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([char for char in s if char.isalpha() or char.isnumeric()])
        reversed_s = s[::-1]
        if reversed_s == s :
            return True
        else: 
            return False