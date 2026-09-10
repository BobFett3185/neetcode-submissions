class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        result =0 
        rows = len(grid)-1
        cols = len(grid[0])-1

        def dfs(r,c):
            if grid[r][c]==0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            x, y, z, a = 0,0,0,0
            if r>0:
                x = dfs(r-1, c)
            if r<rows:
                y = dfs(r+1,c)
            if c>0:
                z = dfs(r, c-1)
            if c<cols:
                a = dfs(r, c+1)
            return 1+a+x+y+z
        
        for r in range(rows+1):
            for c in range(cols+1):
                if (r,c) not in visited and grid[r][c]==1:
                    result = max(result, dfs(r,c))
            
        return result
        