class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] *n # initialize rows for the bottom row (would be all 1s)
        for i in range(m-1): # for all the rows
            newRow = [1]*n # create a new row 
            for j in range(n-2, -1, -1): # only need to start from 2nd to last column -- bc last elemnt of the row will always be 1 
                newRow[j] = newRow[j+1]+ row[j]
            row = newRow
        return row[0]