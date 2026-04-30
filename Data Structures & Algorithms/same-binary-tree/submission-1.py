# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we need to do some kind of traversal algorithm and check that they are the same at each step 
        #we can do root left right preorder traversal pretty easy 

        
        if p is None and q is None: # check if both are none
            return True
        if p is None or q is None: # check if one is none
            return False 

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        