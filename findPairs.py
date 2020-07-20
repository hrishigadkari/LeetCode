class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num = Counter(nums)
        nums = set(nums)
        count = 0
        if (k<0):
            return 0
        if (k == 0):
            for i in num.values():
                if i > 1:
                    count += 1
            return count
        for i in nums:
            if (i + k in nums):
                count += 1
        return count