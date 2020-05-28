class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        for i in range(0,n):
            if A[i] % 2 == 0:
                A.append(A[i])
        
        for i in range(0,n):
            if A[i] % 2 != 0:
                A.append(A[i])
        
        A = A[::-1]
        
        for i in range(0,n):
            A.pop()
      
        return A[::-1]
            