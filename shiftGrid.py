class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid[0])
        flat = sum(grid, [])
        for i in range(0,k):
            app = flat.pop()
            flat = [app] + flat
        return [flat[i:i+n] for i in range(0, len(flat), n)]