class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash1, hash2 = {}, {}
        
        for i in range(len(s)):
            hash1[s[i]] = 1 + hash1.get(s[i],0)
            hash2[t[i]] = 1 + hash2.get(t[i],0)
            
        for i in hash1:
            if hash1[i] != hash2.get(i,0):
                return False
        return True
            
            