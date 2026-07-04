class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows , cols = len(grid), len(grid[0])
        visited = set()
        # islands = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            area = 0
            for i,j in directions:
                area += dfs(r+i,c+j)
            return area + 1

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area,dfs(r,c))
        
        return max_area
        