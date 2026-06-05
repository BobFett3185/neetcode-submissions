class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacv = set() 
        atlv = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r,c, visit,previousHeight):
            if (r,c) in visit or r<0 or c<0 or r == ROWS or c == COLS or heights[r][c] < previousHeight:
                return
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])




        for c in range(COLS):
            dfs(0,c, pacv, heights[0][c])
            dfs(ROWS - 1, c, atlv, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0, pacv, heights[r][0])
            dfs(r, c, atlv, heights[r][COLS-1])

        result =[]
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlv and (r,c) in pacv:
                    result.append((r,c))
        return result

        