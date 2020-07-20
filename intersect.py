class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        if (len(nums1)>len(nums2)):
            nums1 = Counter(nums1)
            for i in nums2:
                if (i in nums1 and nums1[i] > 0):
                    nums1[i] -= 1
                    arr.append(i)
        else:
            nums2 = Counter(nums2)
            for i in nums1:
                if (i in nums2 and nums2[i]>0):
                    nums2[i] -= 1
                    arr.append(i)
        return arr 