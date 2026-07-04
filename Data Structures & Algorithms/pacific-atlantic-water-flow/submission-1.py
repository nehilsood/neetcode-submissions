class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        n,m = len(grid),len(grid[0])
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        pacific, atlantic = set(), set()
        def check(i,j):
            return 0 <= i < n and 0 <=j < m

        def dfs(i,j,visited,prevHeight):
            if (i,j) in visited or not check(i,j) or prevHeight > grid[i][j]:
                return
            visited.add((i,j))
            for x,y in dirs:
                dfs(x+i,y+j,visited,grid[i][j])
        
        for i in range(n):
            dfs(i,0,pacific,grid[i][0])
            dfs(i,m-1,atlantic,grid[i][m-1])
        for j in range(m):
            dfs(0,j,pacific,grid[0][j])
            dfs(n-1,j,atlantic,grid[n-1][j])

        results = []
        for cell in pacific:
            if cell in atlantic and cell not in results:
                results.append(cell)
        
        return results




        