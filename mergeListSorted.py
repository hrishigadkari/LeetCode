class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(0,len(nums2)):
            nums1.pop()
        for i in range(0, len(nums2)):
            nums1.append(nums2[i])
        nums1 = nums1.sort()