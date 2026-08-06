# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node:
                return
            # swap the left and right nodes
            temp = node.left
            node.left = node.right
            node.right = temp
            # then call the same thing for both kids
            invert(node.left)
            invert(node.right)
    
        invert(root)
        return root