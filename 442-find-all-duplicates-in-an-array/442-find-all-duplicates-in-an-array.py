class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        list = []
        for i in nums:
            m = abs(i)
            if nums[m-1] < 0:
                list.append(m)
            else:
                nums[m-1] *= -1
        return list
            
                