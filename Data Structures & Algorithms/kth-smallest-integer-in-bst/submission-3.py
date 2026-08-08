# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # can do in order traversal 
        count = [0]
        result = [0]
        def inOrder(node):
            if not node:
                return 

            

            leftResult = inOrder(node.left)
            if leftResult:
                return leftResult
            
            count[0]+=1
            if count[0]==k:
                return node.val

            rightResult = inOrder(node.right)
            if rightResult:
                return rightResult
            
        return inOrder(root)