class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or(x>0 and x%10 == 0):
            return False
        r = 0 
        while x > r:
            r = r * 10 + x % 10
            x = x // 10 
        return x == r or x == r // 10 