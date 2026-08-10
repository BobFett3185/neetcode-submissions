# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [-1000000] 
     
        #get the max path sum from its left and right children 
        def pathSum(node):
            if not node: 
                return -100000
            left = pathSum(node.left)
            right = pathSum(node.right)

            s =node.val+max(0,left)+ max(0,right)
            currentMax = s + node.val
            result[0] = max(s,result[0])
            return node.val+max(left,right,0)


        pathSum(root)
        return result[0]