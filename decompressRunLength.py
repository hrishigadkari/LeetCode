class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr,arr2 =[],[]
        for i in range(0,len(nums),2):
            arr.append(nums[i])
            arr2.append(nums[i+1])
        return [a for a, f in zip(arr2,arr) for _ in range(f)]