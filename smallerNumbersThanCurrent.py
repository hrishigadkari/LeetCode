class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}
        srt = sorted(nums)
        for i,n in enumerate(srt):
            if n not in dict:
               dict[n] = i
        return [dict[n] for n in nums]