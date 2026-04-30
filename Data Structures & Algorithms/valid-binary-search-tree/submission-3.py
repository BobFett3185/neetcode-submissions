# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def leftSubtreeCheck( root, value): # return whether or not everything in this subtree is less than a value
            if root == None: # if we reach the end return True
                return True
            if root.val >= value: # if at any point the value is greater return false
                return False 
            # we then check both subtrees if those subtrees are less than value
            return leftSubtreeCheck(root.left, value) and leftSubtreeCheck(root.right, value)

        def rightSubtreeCheck( root, value): # return whether or not everything in this subtree is less than a value
            if root == None:
                return True
            if root.val <= value:
                return False 
            
             # we then check both subtrees if those subtrees are less than value
            return rightSubtreeCheck(root.left, value) and rightSubtreeCheck(root.right, value)

        # get the root.val
        # call left and right check for that value 
        # then isValidBST for the children of root
        if not root:
            return True
    
        value = root.val 
        if leftSubtreeCheck(root.left, value) and rightSubtreeCheck(root.right, value):
            return self.isValidBST(root.left) and self.isValidBST(root.right)

        return False

        


            
            