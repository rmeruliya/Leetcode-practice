class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i],0)
            
        for i in hashmap:
            if hashmap[i] >= 2:
                return True
        return False