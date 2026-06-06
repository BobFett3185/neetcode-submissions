class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacv = set() # create a set for each ocean
        atlv = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r,c, visit,previousHeight): # our dfs takes a coordinate, a set and a prev. height
            if (r,c) in visit or r<0 or c<0 or r == ROWS or c == COLS or heights[r][c] < previousHeight:
                return
            # if any of these base cases then invalid and return ^ 
            # if not then add this coordinate to the visited set
            visit.add((r,c))

            # then visit all 4 directions
            dfs(r+1,c, visit, heights[r][c]) # pass current value as previous height for next step
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])

        # for the columns 
        for c in range(COLS):
            dfs(0,c, pacv, heights[0][c]) # start dfs from first row - pac
            dfs(ROWS - 1, c, atlv, heights[ROWS-1][c])# start from bottom row - atl
        for r in range(ROWS): #for num rows 
            dfs(r,0, pacv, heights[r][0]) # start dfs from first column - pac
            dfs(r, c, atlv, heights[r][COLS-1]) # start from last column - atl

        result =[]
        for r in range(ROWS): # go through all pairs 
            for c in range(COLS):
                if (r,c) in atlv and (r,c) in pacv: # if in both then return those
                    result.append((r,c))
        return result

        