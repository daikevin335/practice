class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # if left not a num or letter
            while left < right and not s[left].isalnum():
                left += 1
            # if right not a num or letter
            while right > left and not s[right].isalnum(): 
                right -= 1  
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True