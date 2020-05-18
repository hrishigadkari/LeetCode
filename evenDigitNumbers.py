class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        no = 0
        for i in range(0,n):
            count = 0
            
            while (nums[i] != 0):
                nums[i] = nums[i] // 10
                count += 1
            if count % 2 == 0:
                no += 1
        return no
            