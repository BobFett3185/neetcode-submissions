# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        At each node, find the sum of the left height and right height 
        if that sum is greater then result, update 

        '''
        result =[0] 
        def height(node):
            if not node:
                return 0 
            leftLen = height(node.left)
            rightLen = height(node.right)
            result[0]=max(leftLen+rightLen, result[0])
        
            return max(leftLen,rightLen)+1

        height(root)
        return result[0]

        