class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        t_matrix = zip(*A) 
        return [row for row in t_matrix] 