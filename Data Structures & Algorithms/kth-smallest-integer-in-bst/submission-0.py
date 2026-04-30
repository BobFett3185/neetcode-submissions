# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we go through recursively and perform in order dfs 
        
        result = []

        def dfs(node):
            if not node: # when the node is null
                return
            
            dfs(node.left)# vist left
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result[k-1] # find kth smallest in array


        
        