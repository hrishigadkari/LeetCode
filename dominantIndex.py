class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        for i in nums:
            if i > (mx/2) and i != mx:
                return -1
        return nums.index(mx)