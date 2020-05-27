class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(0, n-1):
            mxm = max(arr[i+1:])
            arr[i] = mxm
        arr[n-1] = -1
        return arr