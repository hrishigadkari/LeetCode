class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        i = 0
        for j in range(0,n):
            if i < j and A[i] <= A[j]:
                i += 1
            if i == n-1:
                return True
        i = 0
        for j in range(0,n):
            if i < j and A[i] >= A[j]:
                i += 1
            if i == n-1:
                return True
        return False
            