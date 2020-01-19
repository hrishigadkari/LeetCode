class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in hash:
                return [hash[rest], i]
            hash[num] = i
        return []