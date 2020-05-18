class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        result = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] == 0:
                counter = 0
            else:
                counter += 1
                result = max(counter, result)
        return result