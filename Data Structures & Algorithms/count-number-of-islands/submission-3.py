class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)-1
        cols = len(grid[0])-1
        result = 0

        def dfs(r,c): # all this does is recursively visit
            grid[r][c] = 0
            if r > 0 and grid[r-1][c]=="1":
                dfs(r-1,c)
            if c > 0 and grid[r][c-1]=="1":
                dfs(r,c-1)
            if r < rows and grid[r+1][c]=="1":
                dfs(r+1,c)
            if c < cols and grid[r][c+1]=="1":
                dfs(r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    result+=1 
                    dfs(r,c) 
                    
    
        return result
