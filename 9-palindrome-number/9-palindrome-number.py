class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev1 = x
        rev = 0
        while x > 0:
            dig = x % 10 
            rev = rev * 10 + dig
            x = x // 10
        print(rev)
        if rev1 == rev:
            return True
        else:
            return False