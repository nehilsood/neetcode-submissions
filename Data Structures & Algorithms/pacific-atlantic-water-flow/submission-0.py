class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c, ocean,prev_h):
            if ((r,c) in ocean or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prev_h):
                return
            ocean.add((r,c))
            for i,j in directions:
                dfs(r+i,c+j,ocean,heights[r][c])
            
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])#top  pacific
            dfs(rows-1,c,atl,heights[rows-1][c])#bottom  atlantic

        for r in range(rows):
            dfs(r,0,pac,heights[r][0]) # left pacific
            dfs(r,cols-1,atl,heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res



        