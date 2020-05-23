class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        n = len(nums)
        while i<n:
            if nums[i-1] == nums[i]:
                nums.remove(nums[i])
                n -= 1
                continue
            i += 1
        return len(nums)