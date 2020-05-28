class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        count = 0
        arr = sorted(heights)
        for i in range(0, n):
            if heights[i] != arr[i]:
                count += 1
        return count