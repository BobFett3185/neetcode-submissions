class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        # another recursive backtracking problem
        #

        def dfs(r, c, i):
            # base cases 
            if i == len(word):
                return True 
            # if out of bounds or already visited or not correct -> return false for that path
            if r >= ROWS or c >= COLS or c < 0 or r < 0 or (r,c) in visited or board[r][c] != word[i]:
                return False
            
            # add to visited path 
            visited.add((r,c))
            # call dfs on all 4 sides 
            result = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visited.remove((r,c))
            return result 

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False


            