class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result =[]
        # basically go until u hit a boundary and at that point you can only go one place 
        
        # here we keep track of our boundary 
        top =0 
        bottom = len(matrix)-1
        left =0 
        right = len(matrix[0])-1
        while top <= bottom and right >= left:
            # repeat -- right down left up --- right down left up 
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top+=1

            # then go down
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right-=1

            # no if condition needed bc they are first to modify those boundaries in the loop 

            # then go left if we have a row there
            if top <= bottom: # we have to check this condition because we are not guaranteed to have 2 rows 
            # this is the first time we could visit an element twice (right and left)
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom-=1

            # then go up if we got a column there
            if left <= right: # same idea of checking if there is a differnt column here than what we already visited
                for i in range(bottom, top-1,-1):
                    result.append(matrix[i][left])
                left+=1

        return result




