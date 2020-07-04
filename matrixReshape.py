class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        a = sum(nums,[])
        if (len(a) != (r*c)):
            return nums
        res = [[0]*c for i in range(r)]
        for i in range(0,len(a)):
            res[i//c][i%c] = a[i]
        return res
            