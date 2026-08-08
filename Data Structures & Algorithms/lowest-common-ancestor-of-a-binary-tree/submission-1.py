# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # top down dfs
        # each node will explore its right and left subtree and check if p and q there
        def dfs(node):
            if not node: # base case
                return
            l = dfs(node.left)
            r = dfs(node.right)
            
            if node == p:
                return p
            if node == q:
                return q
            
            if l and r:
                return node
            elif l:
                return l 
            elif r:
                return r
            

        return dfs(root)