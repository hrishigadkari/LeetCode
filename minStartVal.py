class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        tot,mi = 0,0
        for i in range(0,len(nums)):
            tot += nums[i]
            mi = min(mi,tot)
        return 1-mi