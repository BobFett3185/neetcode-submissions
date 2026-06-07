class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # we are basically checking if the nodes form any cycle 
        # in the undirected graph so we can use a visited set and we need an adjacency list

        adj = [[] for i in range(n)]

        for pair in edges:# since a undirected we mark other edge in both 
            a = pair[0]
            b= pair[1]
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        # use a depth first search to traverse through
        def dfs(i, parent):
            if i in visited:
                return False 

            visited.add(i)
            for neighbor in adj[i]:
                if neighbor != parent:
                    if not dfs(neighbor, i):
                        return False
            
            return True

        if dfs(0, -1) == False:
            return False
        if len(visited) == n:
            return True
        return False
