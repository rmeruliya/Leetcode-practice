class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = s.lower()
        a = ''.join(filter(str.isalnum, f))
      
        l = 0
        r = len(a) - 1
        
        while r >= 0:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True
         
            