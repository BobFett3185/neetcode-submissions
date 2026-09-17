class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS problem 
        # we want to spread out from the rotten fruit until all fruit are rotten 

        # run bfs from all the spots where == 2 and not visited already 
        visited = set()        
        rows = len(grid)
        cols = len(grid[0])
        fresh=0
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c]==1:
                    fresh+=1

        result = 0
        while queue and fresh>0:
            for i in range(len(queue)):
                coord = queue.popleft()
                grid[coord[0]][coord[1]]=0
                if coord[0]>0 and grid[coord[0]-1][coord[1]]==1:
                    fresh-=1 
                    queue.append([coord[0]-1,coord[1]])
                    grid[coord[0]-1][coord[1]]=2
                if coord[0]<=rows-2 and grid[coord[0]+1][coord[1]]==1:
                    fresh-=1 
                    queue.append([coord[0]+1,coord[1]])
                    grid[coord[0]+1][coord[1]]=2
                if coord[1]>0 and grid[coord[0]][coord[1]-1]==1:
                    fresh-=1 
                    queue.append([coord[0],coord[1]-1])
                    grid[coord[0]][coord[1]-1]=2
                if coord[1]<=cols-2 and grid[coord[0]][coord[1]+1]==1:
                    fresh-=1 
                    queue.append([coord[0],coord[1]+1])
                    grid[coord[0]][coord[1]+1]=2
            result+=1 
        print(fresh)
        if fresh!=0:
            return -1
        else:
            return result

        
                

            
            