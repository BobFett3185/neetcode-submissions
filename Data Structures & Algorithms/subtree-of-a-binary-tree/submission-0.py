# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# go through recursively and check each part of root and for those call isSameTree
# recursive within recursive
class Solution: 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # every tree has the empty tree in it 
        if not root: return False # this means theres no root, but there is a subroot, subRoot can't fit inside nothing lol =
        # if we have no root then we also need to return false
        # we move through the root left and right we never mess with subroot left or right


        if self.isSameTree(root, subRoot) is True:
            return True
        
        # we call this recursively on the left and right children
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    # we need to recursively check if the subtree is the same as the
    # this is our helper function 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # we need to do some kind of traversal algorithm and check that they are the same at each step         
            if p is None and q is None: # check if both are none
                return True
            
            if p is None or q is None: # check if one is none if so then return false
                return False 

            if p.val != q.val: # if not same then return false
                return False
            # recursively do for the left and right subtrees of each and return result
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        