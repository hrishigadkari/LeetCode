class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(0, len(nums)):
            if val in nums:
                nums.remove(val)
    
        return len(nums)