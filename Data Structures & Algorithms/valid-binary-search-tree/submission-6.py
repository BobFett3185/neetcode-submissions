# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # need to call dfs with an upper and lower bound which is updated at each step 
        def dfs(node, lower, upper):
            if not node:
                return True
            if node.val >= upper or node.val<=lower:
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root, -1000000, 1000000)

        