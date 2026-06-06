class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we can solve this with topological sort 
        # to keep track of indegree for kahns 
        indegree = [0]*numCourses

        # adjacaency list to keep track of which edges to update at each step 
        adj =[[] for i in range(numCourses)]

        #assign in degree of everything 
        # b is the prereq a is the course : b -> a 
        for a, b in prerequisites:
            indegree[a] +=1
            adj[b].append(a)
        
        q = deque()
        result = []

        # init queue
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while len(q)!=0: # while not empty pop and remove neighbors 
            x = q.popleft()
            result.append(x)
            for neighbor in adj[x]: # for the neighbors of x
                indegree[neighbor] -=1 # reduce the indegree
                if indegree[neighbor] ==0: # if it drops to 0 
                    q.append(neighbor) # add course to the queue

        
        return len(result) == numCourses
                

        

        




