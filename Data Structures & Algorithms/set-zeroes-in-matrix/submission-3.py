class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # we can keep some arrays in the first column and first row 
        # basically go through 
        row = len(matrix)
        col = len(matrix[0])
        rowZero = False

        for r in range(row):
            for c in range(col):
                if matrix[r][c] ==0: # if a zero then set those 2 spots to a zero 
                    matrix[0][c]=0# set this to zero to signifiy the column should be 0
                    if r ==0:
                        rowZero = True # account for if in first row 
                    else:
                        matrix[r][0] =0# set the row to 0 as well 

        # now go through and set entire rows and cols to 0 if those arrays have 0s in them 
        for r in range(1,row):
            if matrix[r][0]==0:
                for c in range(col):
                    matrix[r][c] =0 


        
        for c in range(col):
            if matrix[0][c]==0:
                for r in range(row):
                    matrix[r][c] =0
                
        if rowZero:
            for c in range(col):
                matrix[0][c]=0 
       
        
            



        