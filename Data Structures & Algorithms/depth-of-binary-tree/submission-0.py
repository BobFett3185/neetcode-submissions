# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # we return 1+ to account for the root 
        # we take the max of each the depth of the subtrees and keep doing this recursively
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
#hii