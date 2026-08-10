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
            # go down
            left = pathSum(node.left)
            right = pathSum(node.right)

            # calculate a sum including those vals
            s =node.val+max(0,left)+ max(0,right)
            # update our global max in case our current node is the split point
            result[0] = max(s,result[0])

            #return the biggest branch side in case the split point is above
            return node.val+max(left,right,0)
            
        pathSum(root)
        return result[0]