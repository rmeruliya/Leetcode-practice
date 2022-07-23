class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        j = 0 
        for i in range(len(nums)):
            if nums[i] < target:
                j += 1
        return j
                       