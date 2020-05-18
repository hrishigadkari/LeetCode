class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        for i in range(0,n):
            A[i] = A[i] * A[i]
        return sorted(A)