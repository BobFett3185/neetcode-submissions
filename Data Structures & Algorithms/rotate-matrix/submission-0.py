class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # just gotta transpose then swap the columns about the middle 
        
        # go through the columns and rows and swap the column and row 

        # transpose in place by swapping across diagonal 
        for i in range(len(matrix)):
            for j in range(i+1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # then we need to swap rows by reversing them 
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

        


