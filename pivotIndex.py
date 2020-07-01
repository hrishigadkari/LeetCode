class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = sum(nums)
        lsum = 0
        for i in range(0,len(nums)):
            rsum -= nums[i]
            if i != 0:
                lsum += nums[i-1]
            if (lsum == rsum):
                return i
        return -1
                

            