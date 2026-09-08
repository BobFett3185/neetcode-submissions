class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        result = 0 

        rows = len(grid)-1
        cols = len(grid[0])-1


        def dfs(r,c):
            if grid[r][c]== "0" or (r,c) in visited:
                return 
            
            visited.add((r,c))
            if r<rows:
                dfs(r+1, c)
            if r>0:
                dfs(r-1, c)
            if c<cols:
                dfs(r, c+1)
            if c>0:
                dfs(r, c-1)

        for r in range(rows+1):
            for c in range(cols+1):
                if (r,c) not in visited and grid[r][c]=="1":
                    result+=1
                    dfs(r,c)
        return result



