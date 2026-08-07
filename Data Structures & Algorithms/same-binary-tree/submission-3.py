# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or q and not p: # if one is null and other isn't -> return true
            return False
        if not p and not q: # if both are null then return True
            return True
        if p.val != q.val: # check condition
            return False
        # return left and right subtree results
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)