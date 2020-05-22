class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        i = 0
        while i < n:
            if arr[i] == 0 and i+1 < n:
                arr.insert(i+1,0)
                i += 1
                arr.pop()
            i += 1
#print(arr)