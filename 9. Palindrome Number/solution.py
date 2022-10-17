class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        else:
            
            s_x = str(x)
            s_newx = s_x[::-1]
            if s_x == s_newx:
                return True
            else:
                return False