class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        temp = 0
        
        for i in range(len(s)-1):
            if hashmap[s[i]] < hashmap[s[i+1]]:
                temp -= hashmap[s[i]]
            else:
                temp += hashmap[s[i]]
        return temp + hashmap[s[-1]]
                
             