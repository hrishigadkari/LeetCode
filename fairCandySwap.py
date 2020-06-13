class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(A) - sum(B))/2
        A,B = set(A), set(B)
        for i in B:
            if (i + diff) in A:
                return [i+diff,i]