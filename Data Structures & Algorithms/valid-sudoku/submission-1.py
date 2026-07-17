class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check the rows
        for r in range(9):
            row = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row:
                    return False
                row.add(board[r][c])

        # check the cols
        for c in range(9):
            col = set()
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in col:
                    return False 
                col.add(board[r][c])
        
        starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6) ]
        # trust your intution, just check an offset from all these starting points 
        # much easier to implement and no crazy coordinate finding formula to figure out 
    
        for i, j in starts:
            sq = set() 
            for a in range(3):
                for b in range(3):
                    r= i+a
                    c = j+b
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in sq:
                        return False 
                    else:
                        sq.add(board[r][c])
        return True

                
            
