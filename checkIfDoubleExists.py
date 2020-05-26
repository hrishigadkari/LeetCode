class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(0,n):
            for j in range(0,n):
                if arr[i] == 2 * arr[j] and i !=j:
                    return True
        return False