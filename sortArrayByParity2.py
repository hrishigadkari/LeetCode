class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        E,O,arr = [],[],[]
        for i in range(0,len(A)):
            if A[i] %2 == 0:
                E.append(A[i])
            else:
                O.append(A[i])
        for i in range(0,int(len(A)/2)):
            arr.append(E[i])
            arr.append(O[i])
        return arr
            