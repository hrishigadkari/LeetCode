class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = []
        arr3 = []
        for i in range(0, len(arr2)):
            cnt.append(arr1.count(arr2[i]))
        for i in range(0,len(arr2)):
            arr3 = arr3 + [arr2[i]]*cnt[i]
        arr = [item for item in arr1 if item not in arr2]
        #print(arr)
        return arr3 + sorted(arr)
        