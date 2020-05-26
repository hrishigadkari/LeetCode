class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        if n < 3:
            return False
        count = 0
        for i in range(0, n-1):
            if A[i] < A[i+1]:
                count += 1
        if count == n-1 :
            return False
        
        for i in range(count, n-1):
            if A[i] > A[i+1] and count != 0:
                count += 1    
            else:
                return False
        return count == n-1