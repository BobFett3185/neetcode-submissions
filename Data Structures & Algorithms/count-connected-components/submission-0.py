class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # start with making an adjacency list
        adj = [[]for i in range(n)]

        #undirected so we do for both 
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)


        # create a visited set 
        visited = set() 
        count =0 
        # now we have adj list built so can call dfs on it 
        def dfs(node):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
        for i in range(n):
            if i not in visited:
                count +=1
                dfs(i)
            
            
        return count        
        
