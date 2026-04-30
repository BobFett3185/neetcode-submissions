# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # swap the children
        #recursively do this over and over

        #edge case
        if not root:
            return None

        # swap left and right
        temp = root.left 
        root.left = root.right
        root.right = temp

        #then recursively call on each child
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        