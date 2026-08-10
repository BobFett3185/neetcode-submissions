# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # bottom up dfs so we go down then pass up info about what we foudn
        # each node will explore its right and left subtree and check if p and q there
        # it will return p and q if foud there keep returning that up 
        # when both are found return node
        def dfs(node):
            if not node: # base cases, we return the node up when we find it 
                return
            if node == p:
                return p
            if node == q:
                return q

            # get info from left and right subtrees
            l = dfs(node.left)
            r = dfs(node.right)

            # when these return the function will have 2 values to look at
            # return based on what those values are: 
            
            if l and r: # if this node returns a value for both l and r, return node
                return node
            elif l: # if only l, return left result upwards
                return l 
            elif r: # if only r, return right result upwards
                return r

        return dfs(root)