from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        B = []
        for i in range(0,len(A)):
            B.append(Counter(A[i]))
        result = B[0]
        for i in range(1,len(A)):
            result = result & B[i]
        return list(result.elements())