class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,count,prod1 = 1,0,1
        
        for i in nums:
            prod *= i
            if i == 0:
                count += 1
        if count == 1:
            for i in range(0,len(nums)):
                if nums[i] != 0:
                    prod1 *= nums[i]
            for i in range(0,len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = prod1 
            return nums
        elif count >1:
            return [0]*len(nums)
            
        else:
            for i in range(0,len(nums)):
                nums[i] = (prod // nums[i])
        return nums