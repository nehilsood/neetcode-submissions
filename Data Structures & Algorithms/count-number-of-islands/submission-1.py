class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        n,m = len(grid),len(grid[0])

        def dfs(x,y):
            if 0 <= x < n and 0 <= y < m and grid[x][y] == "1":
                grid[x][y] = "0"
                for i,j in dirs:  
                    dfs(x+i,y+j)
        
        count = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == "1":
                    dfs(x,y)
                    count += 1
        
        return count


        