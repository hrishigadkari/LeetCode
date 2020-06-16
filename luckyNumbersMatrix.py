class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        arr, arr1 = [], []
        for r in matrix:
            arr.append(min(r))
        for r in zip(*matrix):
            arr1.append(max(r))
        print(arr)
        print(arr1)
        return [i for i in arr if i in arr1]