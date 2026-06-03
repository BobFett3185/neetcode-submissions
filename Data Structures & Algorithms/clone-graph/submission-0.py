"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new ={} # hashmap to keep track of our mapping of old to new 

        def clone(node):
            if node in old2new: # if its already in the hashmap then return the node
                return old2new[node] 
            copy = Node(node.val) # if we havent seen that node yet then make it
            old2new[node] = copy # map old to the copy
            for neighbor in node.neighbors: # now for all the neighbors of the node 
                copy.neighbors.append(clone(neighbor)) # clone those nodes
                # and set the copies neighbors to all the copies of the nodes neighbors 
            return copy # we return new node
        
        if node is not None: # return clone of starting node
            return clone(node)
        else:
            return None


            


        

        # just need to do a depth first search 